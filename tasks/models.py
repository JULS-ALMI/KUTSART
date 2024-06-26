from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
#from rest_framework import django


# create your class models here.
class Crear_solicitude(models.Model):
  Asunto = models.CharField(max_length=200)
  Describa_su_solicitud = models.TextField(blank=True)
  Asignado_a_Julian_Albarracin = models.BooleanField(default=True)

  def __str__(self):
    return self.Asunto

class Usuario(models.Model):
  Nombre = models.CharField(max_length=200)
  Cedula = models.IntegerField(validators=[MinValueValidator(1)])
  Correo = models.CharField(max_length=150)
  Numero = models.CharField(max_length=12)


  def __str__(self):
    return self.Nombre

class Dispositivos(models.Model):
  Tipo_de_equipo = models.CharField(max_length=200)
  Marca_del_dispositivo = models.CharField(max_length=150)
  Modelo_del_equipo = models.CharField(max_length=150)
  Numero_serial = models.CharField(max_length=12)

  def __str__(self):
    return self.Tipo_de_equipo

class Institucion(models.Model):

  Administracion = models.BooleanField(default=False)
  IE_LA_ESTRELLITA = models.BooleanField(default=False)
  IE_SAN_JOSE = models.BooleanField(default=False)
  IE_BILBAO = models.BooleanField(default=False)
  IE_CHUNIZA = models.BooleanField(default=False)


class Area(models.Model):
  Rector = models.BooleanField(default=False)
  Cordinador = models.BooleanField(default=False)
  Docente = models.BooleanField(default=False)
  Almacenista = models.BooleanField(default=False)

class Ubicación(models.Model):
  Almacen = models.BooleanField(default=False)
  AudioVisuales = models.BooleanField(default=False)
  Biblioteca = models.BooleanField(default=False)
  Cord_Academica = models.BooleanField(default=False)
  Cord_Convivencia = models.BooleanField(default=False)
  Cuarto_Camaras = models.BooleanField(default=False)
  Deposito = models.BooleanField(default=False)
  Emisora = models.BooleanField(default=False)
  Enfermeria = models.BooleanField(default=False)
  Laboratorio_Biologia = models.BooleanField(default=False)
  Laboratorio_Fisica = models.BooleanField(default=False)
  Laboratorio_Quimica = models.BooleanField(default=False)
  Oratorio = models.BooleanField(default=False)
  Pastoral = models.BooleanField(default=False)
  Psicologia = models.BooleanField(default=False)
  Rectoria = models.BooleanField(default=False)
  Secretaria = models.BooleanField(default=False)
  Sala_Docentes = models.BooleanField(default=False)
  Tecnologia_Primaria = models.BooleanField(default=False)
  Tecnologia_Bachillerato = models.BooleanField(default=False)
  Trabajo_Social = models.BooleanField(default=False)
  Otro = models.CharField(max_length=150)