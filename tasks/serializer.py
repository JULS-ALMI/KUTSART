from rest_framework import serializers
from .models import Crear_solicitude
from tasks import models

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Crear_solicitude
    # fields = ('id','title', 'description', 'done')
    fields = '__all__'