from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from testing.forms import ItemForm
from testing.models import Item

# Create your views here.


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'testing/items_lists.html'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items_lists')
    template_name = 'testing/items_form.html'


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items_lists')
    template_name = 'testing/items_update.html'
    pk_url_kwarg = 'id'



class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('items_lists')
    template_name = 'testing/items_delete.html'
    pk_url_kwarg = 'id'
