# Generated by Django 4.1.1 on 2022-10-23 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Pedido', '0002_tipoentrega_estado_estadopedido_pedido_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='Persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente'),
        ),
    ]
