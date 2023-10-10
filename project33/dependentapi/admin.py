from django.contrib import admin

from dependentapi.models import City, Country, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Country)
admin.site.register(City)

