from django.contrib import admin

from ecommerceapi.models import Product,ProductCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)