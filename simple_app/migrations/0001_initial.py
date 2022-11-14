# Generated by Django 4.1 on 2022-11-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Display",
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
                ("pre", models.CharField(max_length=200)),
                ("major", models.CharField(max_length=500)),
                ("post", models.CharField(max_length=500)),
            ],
        ),
    ]