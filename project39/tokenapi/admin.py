from django.contrib import admin

from tokenapi.models import Bike, BikeColor, BikeModel

# Register your models here.
admin.site.register(Bike)
admin.site.register(BikeColor)
admin.site.register(BikeModel)