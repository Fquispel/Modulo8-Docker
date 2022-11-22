# Generated by Django 4.1.2 on 2022-10-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0005_paciente_alter_medicoespecialista_genero_agendarcita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendarcita',
            old_name='id_paciente',
            new_name='documento_paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='id_paciente',
        ),
        migrations.AddField(
            model_name='paciente',
            name='documento_paciente',
            field=models.CharField(default=1, max_length=35, unique=True),
            preserve_default=False,
        ),
    ]