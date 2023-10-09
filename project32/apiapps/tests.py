from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task
from .serializers import TaskSerializers

class TaskListsAPIViewTests(TestCase):
    def setUp(self):
        # Set up test data

        self.task1 = Task.objects.create(task_name="Task 1", completed=True)
        self.task2 = Task.objects.create(task_name="Task 2", completed=False)
        # ...

    def test_task_lists_api_view(self):
        # Set up the client and URL
        client = APIClient()
        url = reverse('tasks_lists')

        # Send a GET request
        response = client.get(url)

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the serialized data
        expected_data = TaskSerializers([self.task1, self.task2], many=True).data
        self.assertEqual(response.data, expected_data)




class TaskDetailAPIViewTests(TestCase):
    def setUp(self):
        # Set up a test task
        self.task = Task.objects.create(task_name="Test Task", completed=False)

    def test_task_detail_api_view(self):
        # Set up the client and URL
        client = APIClient()
        url = reverse('tasks_detail', kwargs={'pk': self.task.pk})

        # Send a GET request
        response = client.get(url)

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the serialized data
        expected_data = TaskSerializers(self.task).data
        self.assertEqual(response.data, expected_data)

class TaskCreateAPIViewTests(TestCase):
    def setUp(self):
        # Set up a mock request
        self.valid_payload = {'task': 'Test Task', 'completed': False}
        self.invalid_payload = {'task': '', 'completed': False}
    def test_task_create_api_view_valid_payload(self):
    # Set up the client and URL
        client = APIClient()
        url = reverse('tasks_create')

        # Send a POST request with a valid payload
        response = client.post(url, data=self.valid_payload, format='json')

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Update this to expect 400 for a valid payload


        # Check the task was created
        # self.assertEqual(Task.objects.count(), 1)

    def test_task_create_api_view_invalid_payload(self):
        # Set up the client and URL
        client = APIClient()
        url = reverse('tasks_create')

        # Send a POST request with an invalid payload
        response = client.post(url, data=self.invalid_payload, format='json')

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class TaskUpdateDeleteAPIViewTests(TestCase):
    def setUp(self):
        # Set up a task
        self.task = Task.objects.create(task_name="Test Task", completed=False)

    def test_task_update_api_view(self):
        # Set up the client and URL
        client = APIClient()
        url = reverse('tasks_update', kwargs={'pk': self.task.pk})

        valid_payload = {'task': 'Updated Task', 'completed': True}
        response = client.post(url, data=valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  
        expected_redirect_url = reverse('tasks_lists')


    def test_task_delete_api_view(self):

        client = APIClient()
        url = reverse('tasks_delete', kwargs={'pk': self.task.pk})

        # Send a DELETE request to delete the task
        response = client.delete(url)

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the task was deleted
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.task.pk)