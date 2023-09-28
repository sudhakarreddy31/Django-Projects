from urllib.request import Request
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from ajaxcrud.models import StudentInfo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.


class StudentInfoListView(ListView):
    model = StudentInfo
    template_name = 'ajaxcrud/studentinfo_list.html'

from django.views.generic.edit import CreateView
# from .models import StudentInfo
# from django.http import JsonResponse

class StudentInfoCreateView(CreateView):
    model = StudentInfo
    fields = ['name', 'roll_number', 'email', 'marks']

    def form_valid(self, form):
        self.object = form.save()
        data = {'message': 'Item successfully created.'}
        return JsonResponse(data)

    def form_invalid(self, form):
        data = {'error': 'Form is not valid.'}
        return JsonResponse(data, status=400)





class StudentInfoUpdateView(UpdateView):    
    model = StudentInfo
    template_name = 'ajaxcrud/studentinfo_update.html'
    fields = ['name', 'roll_number', 'email', 'marks']

    def form_valid(self, form):
        response = super().form_valid(form)

        # Return a success message
        data = {'success': 'Student information updated successfully.'}
        return JsonResponse(data)

    def form_invalid(self, form):
        data = {'error': 'Form is not valid.'}
        return JsonResponse(data, status=400)

    def get_success_url(self):
        return reverse_lazy('studentslists')


class StudentInfoDeleteView(DeleteView):
    model = StudentInfo  # Specify the model for this view

    def post(self, request, pk):
        student = get_object_or_404(StudentInfo, pk=pk)
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully.'})
























































