# Generated by Django 4.1.3 on 2022-11-13 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pybo", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question", old_name="created_date", new_name="create_date",
        ),
    ]
