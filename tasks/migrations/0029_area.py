# Generated by Django 5.0.6 on 2024-06-23 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0028_alter_crear_solicitude_asignado_a_julian_albarracin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rector', models.BooleanField(default=False)),
                ('Cordinador', models.BooleanField(default=False)),
                ('Docente', models.BooleanField(default=False)),
            ],
        ),
    ]
