import re
from django import forms
from studentapp.models import City, State, Student



class RegistrationForm(forms.Form):

    def validate_username(value):
        if not re.match("^[A-Za-z0-9]+$", value):
            raise forms.ValidationError("Username should only contain alphabets and numbers.")

    def validate_password(value):
        if not re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$", value):
            raise forms.ValidationError("Password should contain at least one alphabet, one number, and one special symbol.")

    def validate_email(value):
        if '@' not in value:
            raise forms.ValidationError("Enter a valid email address.")
        
    username = forms.CharField(max_length=100, validators=[validate_username])
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    email = forms.EmailField(validators=[validate_email])



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()
        self.fields['city'].queryset = City.objects.none()