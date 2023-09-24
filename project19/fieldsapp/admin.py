from django.contrib import admin

from fieldsapp.models import Address, Book, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Book)