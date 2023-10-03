from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy

from chainform.models import City, Country, Person


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.persons_list_url = reverse('persons_list')
        self.person_create_url=reverse_lazy('person_create')
        self.country = Country.objects.create(name='Test Country')
        self.city = City.objects.create(name='Test City', country=self.country)
        self.person = Person.objects.create(name='Initial Name', country=self.country, city=self.city)
        self.person_delete_url = reverse('person_delete', kwargs={'id': self.person.id})

        # URL for updating the person (use the ID of the created person)
        self.person_update_url = reverse('person_update', kwargs={'id': self.person.id})

        # Create some cities associated with the country
        self.city1 = City.objects.create(name='City 1', country=self.country)
        self.city2 = City.objects.create(name='City 2', country=self.country)




    def test_person_list_view_GET(self):
        response = self.client.get(self.persons_list_url)
        self.assertEqual(response.status_code, 200)  # Assuming 200 is the expected response code
        self.assertTemplateUsed(response,'chainform/persons_lists.html')
        # You can add more assertions based on your specific view behavior and template rendering


    def test_person_create_view_POST(self):
        response = self.client.post(self.person_create_url,{
            'name': 'Test name',
            'birthdate': 'mm-yyyy-dd',
            'country':'Test Country',
            'city':'Test City'
        })
        self.assertEqual(response.status_code,200)

    def test_person_update_view_POST(self):
        # Simulate updating the person
        updated_name = 'Updated Name'
        response = self.client.post(self.person_update_url, {
            'name': updated_name,
            'birthdate': '2023-10-03',  # Adjust to a valid date format
            'country': self.country.id,
            'city': self.city.id
        })

        # Check if the person was updated successfully
        self.assertEqual(response.status_code, 302)
        self.person.refresh_from_db()  # Refresh the person instance from the database
        self.assertEqual(self.person.name, updated_name)

        
    def test_item_delete_view_DELETE(self):
        response = self.client.delete(self.person_delete_url )
        self.assertEqual(response.status_code, 302) 