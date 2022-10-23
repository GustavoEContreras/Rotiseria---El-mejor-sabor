# Generated by Django 4.1.1 on 2022-10-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Normal', 'Normal'), ('Celiaco', 'Celiaco'), ('Vegetariano', 'Vegetariano'), ('Diabetico', 'Diabetico')], default='Normal', max_length=15, unique=True)),
            ],
        ),
    ]
