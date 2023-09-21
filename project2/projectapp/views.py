from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from projectapp.models import Company
# Create your views here.


class CompanyListView(ListView):
    model = Company
    template_name = '/projectapp/company_list.html'



class CompanyDetailView(DetailView):
    model = Company
    template_name = 'projectapp/company_detail.html'


class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'ceo', 'location', 'number']
    template_name = 'projectapp/company_create.html'



class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'ceo', 'location', 'number']
    template_name = 'projectapp/company_create.html'


class CompanyDeleteView(DeleteView):
    model= Company 
    template_name = 'projectapp/company_delete.html'
    success_url = reverse_lazy('listview')
    
