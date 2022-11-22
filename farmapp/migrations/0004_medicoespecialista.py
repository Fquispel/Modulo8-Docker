# Generated by Django 4.1.2 on 2022-10-08 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0003_alter_medicamento_nombre_medicamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicoEspecialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula_medico', models.CharField(max_length=35)),
                ('nombre_medico', models.CharField(max_length=75)),
                ('paterno_medico', models.CharField(max_length=75)),
                ('materno_medico', models.CharField(max_length=75)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='M', max_length=25)),
                ('contacto', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
