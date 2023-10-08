from django import forms

from apiapp.models import StrangersThings

class StrangersThingsForm(forms.ModelForm):
    class Meta:
        model = StrangersThings
        fields ='__all__'

        