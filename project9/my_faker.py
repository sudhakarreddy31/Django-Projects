import os
import django
from faker import Faker
import random

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project9.settings')

# Configure Django settings
django.setup()

# Import your Django models after configuring Django settings
from ormsapp.models import Employee  # Adjust the import path based on your project structure

def generate_fake_employees():
    fake = Faker()

    south_indian_first_names = ['Ravi', 'Suresh', 'Krishna', 'Lakshmi', 'Saravanan', 'Ananya', 'Aruna', 'Shankar', 'Padma', 'SudhakarReddy']
    south_indian_locations = ['Hyderabad', 'PUne', 'Keralam', 'Ameravathi', 'Kadapa', 'Bangulour']

    for _ in range(10):  # Generate 10 fake employees
        employee_id = fake.random_number(digits=5)
        employee_name = random.choice(south_indian_first_names)  # Randomly choose a name from the list
        employee_location = random.choice(south_indian_locations)
        employee_salary = fake.random_int(min=30000, max=100000)

        # Create an Employee instance and save it to the database
        employee = Employee(
            emp_number=employee_id,
            emp_name=employee_name,
            emp_location=employee_location,
            emp_salary=employee_salary
        )
        employee.save()

    print('Fake employee data generation complete.')

if __name__ == '__main__':
    generate_fake_employees()
