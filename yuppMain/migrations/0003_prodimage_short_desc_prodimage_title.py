# Generated by Django 4.0.3 on 2022-04-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuppMain', '0002_prodimage_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodimage',
            name='short_desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prodimage',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]