# Register your models here.
from django.contrib import admin
from tasks import models

admin.site.register(models.Crear_solicitude)

#________________________________________________________

admin.site.register(models.Usuario)

#________________________________________________________

admin.site.register(models.Dispositivos)

#________________________________________________________


admin.site.register(models.Institucion)
#________________________________________________________

admin.site.register(models.Ubicación)