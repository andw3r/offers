from django.db import models
import uuid
from rest_framework import serializers

class OfferProperty(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
  logotype = models.URLField(max_length=200)
  deeplink_name = models.CharField(max_length=255)
  salesmanager_hide = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  rate_label = models.CharField(max_length=255)
  rate_from = models.CharField(max_length=255)
  rate_value = models.CharField(max_length=255)
  rate_desc = models.CharField(max_length=255)
  amount_label = models.CharField(max_length=255)
  amount_to = models.CharField(max_length=255)
  amount_value = models.CharField(max_length=255)
  amount_desc = models.CharField(max_length=255)
  term_label = models.CharField(max_length=255)
  term_value = models.CharField(max_length=255)
  term_desc = models.CharField(max_length=255)
  info_line_0 = models.CharField(max_length=255)
  info_line_1 = models.CharField(max_length=255)
  info_line_2 = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  additional_link = models.CharField(max_length=255)
  btn_title = models.CharField(max_length=255)
  special = models.CharField(max_length=255)
  special_label = models.CharField(max_length=255)
  visible = models.CharField(max_length=255)
  loader = models.CharField(max_length=255)
  number = models.CharField(max_length=255)
  template = models.CharField(max_length=255)
  iframe_enable = models.CharField(max_length=255)


class Offer(models.Model):
  name = models.CharField(default='Offer', max_length=120)
  offers = models.ManyToManyField(OfferProperty)

class OfferPropertySerializer(serializers.ModelSerializer):
  
  class Meta:
    model = OfferProperty
    fields = "__all__"

class OfferSerializer(serializers.ModelSerializer):

  property = OfferPropertySerializer(many=True)

  class Meta:
    model = Offer
    field = "__all__"

    def create(self, validate_data):

      properties = validate_data.pop('property')
      offer_instance = Offer.objects.create(**validate_data)

      for property in properties:

        property_instance = property.objects.create(**property)

        offer_instance.property.add(property_instance.id)

        offer_instance.save()

        return offer_instance