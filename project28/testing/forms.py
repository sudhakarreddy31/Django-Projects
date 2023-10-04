from typing import Any
from django import forms

from testing.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def clean(self):
        clean_data = super().clean()
        name_data = self.cleaned_data['name']
        description_data = self.cleaned_data['description']

        if len(name_data) < 3:
            raise forms.ValidationError('The Name Should Be More Than Three Charactors..!')
        if len(description_data) < 10:
            raise forms.ValidationError('The Description is more than 10 charactors..!')