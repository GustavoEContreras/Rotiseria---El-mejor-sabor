# Generated by Django 4.1.1 on 2022-10-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0003_alter_direccion_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='tipoTelefono',
            field=models.CharField(choices=[('Fijo', 'Fijo'), ('Celular', 'Celular')], default='Celular', max_length=7),
        ),
    ]
