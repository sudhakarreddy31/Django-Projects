from django.contrib import admin
from MTMapp.models import Category,Manufacturer,Product
# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Product)
