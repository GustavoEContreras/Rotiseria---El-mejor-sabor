# Generated by Django 4.1.1 on 2022-11-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plato', '0003_alter_plato_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precio',
            name='precio',
            field=models.IntegerField(),
        ),
    ]