from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import University, Student

class UniversityListView(ListView):
    model = University
    template_name = 'projectapp/university_list.html'
    context_object_name = 'universities'

class UniversityDetailView(DetailView):
    model = University
    template_name = 'projectapp/university_detail.html'
    context_object_name = 'university'

class UniversityCreateView(CreateView):
    model = University
    template_name = 'projectapp/university_form.html'
    fields = ['name', 'location']

class UniversityUpdateView(UpdateView):
    model = University
    template_name = 'projectapp/university_form.html'
    fields = ['name', 'location']

class UniversityDeleteView(DeleteView):
    model = University
    template_name = 'projectapp/university_confirm_delete.html'
    success_url = reverse_lazy('university-list')

class StudentListView(ListView):
    model = Student
    template_name = 'projectapp/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'projectapp/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'projectapp/student_form.html'
    fields = ['first_name', 'last_name', 'universities_attended', 'primary_university']

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'projectapp/student_form.html'
    fields = ['first_name', 'last_name', 'universities_attended', 'primary_university']

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'projectapp/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
