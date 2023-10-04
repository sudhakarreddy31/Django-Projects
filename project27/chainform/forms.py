import datetime
from typing import Any
from django import forms

from chainform.models import City, Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()


        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

    def clean(self):
        cleaned_data = super().clean()
        name_data = self.cleaned_data['name']
        # date = self.cleaned_data['birthdate']
        # country = self.cleaned_data['country']
        # city = self.cleaned_data['city']

        if not name_data.replace(" ", "").isalpha():
            raise forms.ValidationError("Name must contain only letters and spaces.")
        
