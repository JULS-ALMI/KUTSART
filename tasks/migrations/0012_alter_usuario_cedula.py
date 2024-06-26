# Generated by Django 5.0.6 on 2024-06-21 03:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_alter_usuario_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Cedula',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
    ]
