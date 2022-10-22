# Generated by Django 4.1.1 on 2022-10-22 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoEntrega', models.CharField(choices=[('Delivery', 'Delivery'), ('Retiro', 'Retiro')], default='Retiro', max_length=8, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='estado',
            name='estadoPedido',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En preparación', 'En preparación'), ('En camino', 'En camino'), ('Entregado', 'Entregado'), ('Devuelto', 'Devuelto'), ('Cancelado', 'Cancelado')], default='Pendiente', max_length=15, unique=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='Estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pedido.estado'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='TipoEntrega',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pedido.tipoentrega'),
        ),
    ]
