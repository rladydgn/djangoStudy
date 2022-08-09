# Generated by Django 4.0.3 on 2022-08-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('important', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
