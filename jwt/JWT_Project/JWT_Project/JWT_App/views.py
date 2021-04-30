

from django.shortcuts import render

from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication

class Emp_ViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
