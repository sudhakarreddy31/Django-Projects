from django.contrib import admin
from movieapp.models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields = ['movie_title','release_year','actor_name','director']


admin.site.register(Movie,MovieAdmin)
