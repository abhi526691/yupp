from tkinter import N
from django.db import models

# Create your models here.

class contacts(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class products(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class prodImage(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    short_desc = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='product/')
    
    def __str(self):
        return self.product.name
