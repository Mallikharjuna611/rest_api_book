
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ModelViewSet_App.models import Emp
from .serializers import EmpSerializer

class EmpViewSet(ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


