from django.contrib import admin

from studentapp.models import Branch, City, Country, State, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Branch)



