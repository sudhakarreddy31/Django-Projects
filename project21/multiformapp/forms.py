from django import forms

from multiformapp.models import StudentInfo


class FirstStudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo 
        fields = ['first_name','last_name','student_id','email','phone_number']

class SecondStudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo 
        fields = ['qualification','subject','age','location']
