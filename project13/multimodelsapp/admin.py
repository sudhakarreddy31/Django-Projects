from django.contrib import admin

from multimodelsapp.models import Customer, Order, Product

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)

