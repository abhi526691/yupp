from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(contacts)
admin.site.register(products)
admin.site.register(prodImage)