from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.shortcuts import render

from dropdownlist.models import Branch, Student
from dropdownlist.forms import StudentForm

# Create your views here.


class StudentListView(ListView):
    model = Student
    form_class = StudentForm
    context_object_name = 'students'
    template_name = 'dropdownlist/student_lists.html'




class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    context_object_name = 'student'
    template_name = 'dropdownlist/student_form.html'
    success_url = reverse_lazy('student_lists')



class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm  
    template_name = 'dropdownlist/student_update.html'
    success_url = reverse_lazy('student_lists')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'dropdownlist/student_confirm_delete.html'
    success_url = reverse_lazy('student_lists')



def load_branches(request):
    collage_id = request.GET.get('collage')
    branches = Branch.objects.filter(collage_id=collage_id).order_by('name')
    return render(request, 'dropdownlist/branch_dropdown_list_options.html', {'branches': branches})
