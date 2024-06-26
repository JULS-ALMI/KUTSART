#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Crear_solicitude

class TaskView(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  queryset = Crear_solicitude.objects.all()