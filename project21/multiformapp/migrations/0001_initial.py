# Generated by Django 4.2.5 on 2023-09-26 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('student_id', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.BigIntegerField(default=10)),
                ('qualification', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('created_by', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.timezone)),
            ],
        ),
    ]
