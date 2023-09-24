from django import forms
from fieldsapp.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields='__all__'        
    