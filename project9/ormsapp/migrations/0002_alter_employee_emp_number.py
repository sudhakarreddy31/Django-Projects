# Generated by Django 4.2.5 on 2023-09-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_number',
            field=models.IntegerField(),
        ),
    ]