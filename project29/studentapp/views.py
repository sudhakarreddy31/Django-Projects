from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from studentapp.models import City, State, Student
from studentapp.forms import LoginForm, RegistrationForm, StudentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.


class RegistrationView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request,'studentapp/registration_form.html',{'form':form})
    
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect('login')  
        return render(request, 'studentapp/registration_form.html', {'form': form})



class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'studentapp/login_form.html',{'form':form})
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('student_lists') 
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'studentapp/login_form.html', {'form': form})

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'studentapp/students_lists.html'


class StudentCreateView(CreateView):
    model = Student
    form = StudentForm()
    fields = '__all__'
    success_url = 'student_lists'
    template_name = 'studentapp/student_form.html'


def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'studentapp/state_dropdown_list_options.html', {'states': states})

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(city_id=state_id).order_by('name')
    return render(request, 'studentapp/city_dropdown_list_options.html', {'cities': cities})


class StudentUpdateView(UpdateView):
    model = Student
    form = StudentForm()
    fields = '__all__'
    template_name = 'studentapp/student_update.html'
    pk_url_kwarg = 'id'


    def get_success_url(self):
        return reverse('student_lists')  # Assuming 'student_lists' is the correct URL name

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')  # Retrieve the pk from URL
        return Student.objects.get(pk=pk)

class StudentDeleteView(DeleteView):
    model = Student
    form = StudentForm()
    fields = '__all__'
    template_name = 'studentapp/student_delete.html'
    pk_url_kwarg = 'id'


    def get_success_url(self):
        return reverse('student_lists')  # Assuming 'student_lists' is the correct URL name

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')  # Retrieve the id from URL
        return Student.objects.get(pk=id)



























































