# Generated by Django 5.0.6 on 2024-06-23 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0026_rename_guardar_crear_solicitude_persona_quien_lo_atiende_julian_albarracin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crear_solicitude',
            old_name='Persona_quien_lo_atiende_Julian_Albarracin',
            new_name='Asignado_a_Julian_Albarracin',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Administracion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='IE_BILBAO',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='IE_CHUNIZA',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='IE_LA_ESTRELLITA',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='IE_SAN_JOSE',
        ),
    ]
