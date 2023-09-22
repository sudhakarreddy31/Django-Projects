from django.contrib import admin

from actressapp.models import Actress, Director, Movie

# Register your models here.

admin.site.register(Actress)
admin.site.register(Director)
admin.site.register(Movie)