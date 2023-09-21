import os
import django
from faker import Faker
import random

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project10.settings')


# Configure Django settings
django.setup()

# Import your Django models after configuring Django settings
from ormscrud.models import Employee  # Adjust the import path based on your project structure

def generate_fake_employees():
    fake = Faker()

    south_indian_names = ['Ravi', 'Suresh', 'Krishna', 'Lakshmi', 'Saravanan', 'Ananya', 'Aruna', 'Shankar', 'Padma', 'SudhakarReddy']
    south_indian_locations = ['Chennai', 'Bangalore', 'Hyderabad', 'Coimbatore', 'Mysore', 'Madurai', 'Trivandrum', 'Vizag']

    for _ in range(10):  # Generate 10 fake employees
        employee_id = fake.random_number(digits=5)
        employee_name = random.choice(south_indian_names)
        employee_location = random.choice(south_indian_locations)
        employee_salary = fake.random_int(min=30000, max=100000)

        Employee.objects.create(
            eno=employee_id,
            ename=employee_name,
            esal=employee_salary,
            eaddr=employee_location
        )

    print('Fake employee data generation complete.')

if __name__ == '__main__':
    generate_fake_employees()
