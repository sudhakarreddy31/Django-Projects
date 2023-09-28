from django import forms

from ajaxcrud.models import StudentInfo


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        