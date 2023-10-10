from django.contrib import admin

from dropdownapi.models import City, Country, Person

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)