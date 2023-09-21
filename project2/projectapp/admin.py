from django.contrib import admin
from projectapp.models import Company

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'ceo', 'number']


admin.site.register(Company,CompanyAdmin)