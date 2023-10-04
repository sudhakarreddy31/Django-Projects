from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy
from dropdownlist.models import Branch, Collage, Student


# Create your tests here.

class TestViews(TestCase):
    # setup for client using for HttpResponse
    def setUp(self):
        self.client=Client()

        # write urls 
        self.student_lists_url=reverse('student_lists')     #list urls
        self.student_create_url=reverse_lazy('student_create')      #createe urls

        self.collage = Collage.objects.create(name='Test Collage')                  #create instance for college field
        self.branch = Branch.objects.create(name='Test Branch', collage=self.collage)   #create instance for branc field
        

        # Create a student for testing
        self.student = Student.objects.create(
            name='UpdatedTest Name',
            roll_number=123,
            data_of_birth='1997-11-13',
            collage=self.collage,
            branch=self.branch
        )

        # print(f'Student PK: {self.student.pk}')
        # print(f'Student Name: {self.student.name}')

        # URL for updating the student
        self.student_update_url = reverse('student_update', kwargs={'pk': self.student.pk})        
        self.student_delete_url= reverse('student_delete', kwargs={'pk': self.student.pk})

    def test_student_list_View_GET(self):
        response = self.client.get(self.student_lists_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'dropdownlist/student_lists.html')


    def test_student_create_View_POST(self):
        response = self.client.post(self.student_create_url,{
            'name':'Test Name',
            'roll_number':'Test roll_number',
            'data_of_birth':'Test data_of_birth',
            'collage':'Test collage',
            'branch':'Test branch'

        })
        self.assertEqual(response.status_code,200)



    def test_student_update_view_POST(self):
        # Updated student data
        updated_data = {
            'name': 'UpdatedTest Name',
            'roll_number': 123,  
            'date_of_birth': '1997-11-13', 
            'collage': self.collage.id,
            'branch': self.branch.id
        }
        response = self.client.post(self.student_update_url, updated_data)
        self.assertEqual(response.status_code, 200)  

        updated_student = Student.objects.get(pk=self.student.pk)
        self.assertEqual(updated_student.name, updated_data['name'])
        self.assertEqual(updated_student.roll_number, updated_data['roll_number'])
        self.assertEqual(str(updated_student.data_of_birth), updated_data['date_of_birth']) 
        self.assertEqual(updated_student.collage.id, updated_data['collage'])
        self.assertEqual(updated_student.branch.id, updated_data['branch'])


    def test_student_update_view_DELETE(self):
        response = self.client.post(self.student_delete_url)
        self.assertRedirects(response, reverse('student_lists'), status_code=302)








