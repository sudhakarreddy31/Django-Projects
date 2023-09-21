from django import forms

from abstactmultiapp.models import Book
# from django.forms import form

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'



    












