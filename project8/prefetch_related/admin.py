from django.contrib import admin

from prefetch_related.models import Book, Store

# Register your models here.


admin.site.register(Book)
admin.site.register(Store)