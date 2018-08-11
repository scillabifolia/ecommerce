from django.contrib import admin
#if I would have been in another app I would have writte products.models
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
