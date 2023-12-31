# Generated by Django 4.2.5 on 2023-10-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_id", models.PositiveIntegerField()),
                ("name", models.CharField(max_length=100)),
                ("cost", models.DecimalField(decimal_places=2, max_digits=6)),
                ("date", models.DateField()),
                ("description", models.TextField()),
            ],
        ),
    ]
