# Generated by Django 4.2 on 2023-07-27 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_tarea_contacto_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Email',
            new_name='email',
        ),
    ]