# Generated by Django 4.2.5 on 2023-10-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chainform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AddField(
            model_name='person',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]