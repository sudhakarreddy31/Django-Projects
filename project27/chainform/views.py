from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from chainform.models import City, Person
from chainform.forms import PersonForm
# Create your views here.


class PersonListView(ListView):
    model = Person
    context_object_name = 'persons'
    template_name = 'chainform/persons_lists.html'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('persons_list')
    template_name = 'chainform/person_form.html'

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('persons_list')
    template_name = 'chainform/person_update.html'
    pk_url_kwarg = 'id'


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'chainform/city_dropdown_list_options.html', {'cities': cities})

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('persons_list')
    template_name = 'chainform/person_delete.html'
    pk_url_kwarg = 'id'
