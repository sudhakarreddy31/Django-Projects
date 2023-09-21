from django import forms
from multimodelapp.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


