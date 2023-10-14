# Generated by Django 4.2.5 on 2023-10-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
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
                ("category_name", models.CharField(max_length=100)),
                ("category_id", models.PositiveSmallIntegerField()),
            ],
        ),
    ]