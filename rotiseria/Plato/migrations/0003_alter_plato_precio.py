# Generated by Django 4.1.1 on 2022-10-25 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Plato', '0002_rename_codigoplato_precio_plato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='Precio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Plato.precio'),
        ),
    ]