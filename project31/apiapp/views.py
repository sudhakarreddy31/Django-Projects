from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apiapp.models import StrangersThings
from apiapp.forms import StrangersThingsForm

# Create your views here.

class StrnagerListView(ListView):
    model = StrangersThings
    context_object_name = 'stangers'
    template_name = ('apiapp/stangers_lists.html')

class StrnagerCreateView(CreateView):
    model = StrangersThings
    form = StrangersThingsForm
    fields="__all__"
    success_url =  'stanger_lists'
    template_name = 'apiapp/stanger_create.html'


class StrnagerUpdateView(UpdateView):
    model = StrangersThings
    form = StrangersThingsForm
    fields="__all__"
    success_url = reverse_lazy('stanger_lists')  # Use reverse_lazy to resolve URLs by name
    template_name = 'apiapp/stanger_update.html'



class StrnagerDeleteView(DeleteView):
    model = StrangersThings
    form = StrangersThingsForm()
    fields = '__all__'
    template_name = 'apiapp/stanger_delete.html'
    success_url = reverse_lazy('stanger_lists')  # Use reverse_lazy to resolve URLs by name



































