from django.contrib import admin
from projectapp.models import University,Student

# Register your models here.


class UniversityAdmin(admin.ModelAdmin):
    model = University
    fields = ['name','location']



class StudentAdmin(admin.ModelAdmin):
    model = Student
    fields = ['first_name','last_name','universities_attended','primary_university']



admin.site.register(University,UniversityAdmin)
admin.site.register(Student,StudentAdmin)