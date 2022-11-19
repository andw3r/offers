# Generated by Django 4.1.3 on 2022-11-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_offerproperties_additional_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerproperties',
            name='additional_link',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='amount_desc',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='amount_label',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='amount_to',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='amount_value',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='btn_title',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='deeplink_name',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='iframe_enable',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='info_line_0',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='info_line_1',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='info_line_2',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='link',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='loader',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='logotype',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='number',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='rate_desc',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='rate_from',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='rate_label',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='rate_value',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='salesmanager_hide',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='special',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='special_label',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='template',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='term_desc',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='term_label',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='term_value',
        ),
        migrations.RemoveField(
            model_name='offerproperties',
            name='visible',
        ),
        migrations.AlterField(
            model_name='offerproperties',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='offerproperties',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]