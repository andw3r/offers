from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Offer

# Create your views here.
def json(request):
  data = list(Offer.object.values())
  return JsonResponse(data, safe=False)