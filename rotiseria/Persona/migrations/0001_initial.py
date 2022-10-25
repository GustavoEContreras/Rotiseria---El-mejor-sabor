# Generated by Django 4.1.1 on 2022-10-21 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barrio', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=30)),
                ('numero', models.DecimalField(decimal_places=0, max_digits=5)),
                ('localidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cuil', models.DecimalField(decimal_places=0, max_digits=8, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='F', max_length=1)),
                ('fechaDeNacimiento', models.DateField()),
                ('Direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Persona.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(choices=[('Norte', 'Norte'), ('Sur', 'Sur'), ('Oeste', 'Oeste'), ('Este', 'Este')], default='Norte', max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('numeroTelefono', models.DecimalField(decimal_places=0, max_digits=13, primary_key=True, serialize=False, unique=True)),
                ('tipoTelefono', models.CharField(choices=[('Fijo', 'Fijo'), ('Celular', 'Celular')], default='Celular', max_length=7, unique=True)),
                ('Persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Persona.persona')),
            ],
        ),
        migrations.AddField(
            model_name='direccion',
            name='Zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Persona.zona'),
        ),
    ]