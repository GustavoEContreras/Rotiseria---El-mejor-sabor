# Generated by Django 4.1.1 on 2022-10-22 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Plato', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plato',
            old_name='tipoMenu',
            new_name='Menu',
        ),
        migrations.RenameField(
            model_name='plato',
            old_name='precioPlato',
            new_name='Precio',
        ),
        migrations.RenameField(
            model_name='plato',
            old_name='tipoPlato',
            new_name='TipoPlato',
        ),
    ]
