from django.contrib import admin
#if I would have been in another app I would have writte products.models
from .models import Product
# Register your models here.

admin.site.register(Product)
