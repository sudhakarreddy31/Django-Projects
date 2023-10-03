from django.test import Client, TestCase
from django.urls import reverse, reverse_lazy
from testing.models import Item

# Create your tests here.

class TestView(TestCase):
    # setup for client 
    def setUp(self):
        self.client = Client()

        # Write urls 
        self.items_lists_url = reverse('items_lists')   #name='items_lists' in urls
        self.item_create_url = reverse_lazy('item_create')
        self.item = Item.objects.create(name='Test Item', description='Test Description')        
        self.item_update_url = reverse('item_update', kwargs={'id': self.item.pk})
        self.item_delete_url= reverse('item_delete', kwargs={'id': self.item.pk})




        
    def test_item_list_view_GET(self):
        response = self.client.get(self.items_lists_url)
        # write asserts 
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'testing/items_lists.html')

    def test_item_create_view_POST(self):
        response = self.client.post(self.item_create_url,{
            'name':'Test Item',
            'description':'Test Description'
        })
        self.assertEqual(response.status_code,302)
        # self.assertTemplateUsed(response,'testing/items_form.html') 

    def test_item_update_view_GET(self):
        response = self.client.get(self.item_update_url)
        self.assertEqual(response.status_code, 200)  # Assuming 200 is the expected response code
        self.assertTemplateUsed(response, 'testing/items_update.html')


    def test_item_update_view_POST(self):
        # Modify the item's data
        updated_name = 'Updated Test Item'
        updated_description = 'Updated Test Description'

        response = self.client.post(self.item_update_url, {
            'name': updated_name,
            'description': updated_description
        })

        # Reload the item from the database to get the updated values
        self.item.refresh_from_db()

        self.assertEqual(response.status_code, 302)  # Assuming 302 is the expected response code (redirect)
        self.assertEqual(self.item.name, updated_name)  # Check if the item is updated correctly
        self.assertEqual(self.item.description, updated_description)



    def test_item_delete_view_DELETE(self):
        response = self.client.delete(self.item_delete_url)
        self.assertEqual(response.status_code, 302) 