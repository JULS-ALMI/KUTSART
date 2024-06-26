# Generated by Django 5.0.6 on 2024-06-23 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_alter_usuario_cedula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Administracion', models.BooleanField(default=False)),
                ('IE_LA_ESTRELLITA', models.BooleanField(default=False)),
                ('IE_SAN_JOSE', models.BooleanField(default=False)),
                ('IE_BILBAO', models.BooleanField(default=False)),
                ('IE_CHUNIZA', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Cedula',
            field=models.IntegerField(max_length=20, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
