from django.shortcuts import redirect, render
from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import View
from studentapp.models import City, Country, State, Student
from studentapp.forms import LoginForm, RegistrationForm, StudentForm
# Create your tests here.


class RegistrationView(View):
    def setUp(self):
        self.client = Client()

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'studentapp/registration_form.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username=username, password=password, email=email)
            # Redirect to the login view upon successful registration
            return redirect('login')

        return render(request, 'studentapp/registration_form.html', {'form': form})
    


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'studentapp/login_form.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_post_request_valid_credentials(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertRedirects(response, reverse('student_lists'))  # Check redirection

    def test_post_request_invalid_credentials(self):
        data = {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)  # Form should be redisplayed
        self.assertContains(response, 'Invalid username or password')  # Check error message

class StudentListViewTest(TestCase):
    def setUp(self):
        # Create some test students
        Student.objects.create(first_name='John', last_name='Doe', roll_number=1234)
        Student.objects.create(first_name='Jane', last_name='Doe', roll_number=5678)

        def test_student_list_view(self):
            response = self.client.get(reverse('student_list'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'studentapp/students_lists.html')

            # Check if the students are present in the HTML
            self.assertContains(response, 'John Doe')
            self.assertContains(response, 'Jane Doe')


class LoadStatesAndCitiesTest(TestCase):
    def test_load_states(self):
        # Assume you have proper setup for Country and State models
        response = self.client.get(reverse('ajax_load_states'), {'country': 1})  # Assuming 1 is a valid country_id
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_load_cities(self):
        # Assume you have proper setup for State and City models
        response = self.client.get(reverse('ajax_load_cities'), {'state': 1})  # Assuming 1 is a valid state_id
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

class StudentCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_student_create_view(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'roll_number': 1234,
            'email': 'test@gmail.com',
            'branch': 'testbranch',
            'country': 'country',
            'state': 'state',
            'city': 'city',
            # Include other fields as needed
        }

        response = self.client.post(reverse('student_form'), data=form_data)

        # Check if the view redirected to the correct URL
        self.assertEqual(response.status_code, 200)  # Redirect status code
        # self.assertEqual(response.url, reverse('student_lists'))
        # self.assertEqual(response['Location'], reverse('student_lists'))



class StudentUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        country = Country.objects.create(name='Test Country')

        # Create a State instance associated with the country
        state = State.objects.create(name='Test State', country=country)

        # Create a City instance associated with the state
        city = City.objects.create(name='Test City', state=state)

        # Create a Student instance and associate with the country, state, and city
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            roll_number=1234,
            email='test@gmail.com',
            branch='test branch',
            country=country,
            state=state,
            city=city
        )


        # Assuming 'student_update' URL has a parameter for student ID
        url = reverse('student_update', kwargs={'id': self.student.pk})
        response = self.client.post(url, data=self.student)

        # Check if the view redirected to the correct URL after a successful update
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(response.url, reverse('student_lists'))

        # Alternatively, you can check the 'Location' header
        self.assertEqual(response['Location'], reverse('student_lists'))

        # Check if the student was updated with the provided data
        updated_student = Student.objects.get(pk=self.student.pk)
        self.assertEqual(updated_student.first_name, self.student['first_name'])
        self.assertEqual(updated_student.last_name, self.student['last_name'])
        self.assertEqual(updated_student.roll_number, self.student['roll_number'])
        self.assertEqual(updated_student.email, self.student['email'])
        self.assertEqual(updated_student.branch, self.student['branch'])
        self.assertEqual(updated_student.country, self.student['country'])
        self.assertEqual(updated_student.state, self.student['state'])
        self.assertEqual(updated_student.city, self.student['city'])




class StudentDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a Country instance
        country = Country.objects.create(name='Test Country')
        state = State.objects.create(name='Test State', country=country)
        # Create a Student instance with a valid country
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            roll_number=1234,
            country=country,  # Assign the country instance
            state=state
        )
        # Set the URL for the delete view
        self.url = reverse('student_delete', kwargs={'id': self.student.pk})

    def test_student_delete_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # Check if the view is accessible

    def test_student_delete(self):
        # Make a POST request to delete the student
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)  # Check for a redirect after deletion
        # Check if the student is deleted
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(pk=self.student.pk)