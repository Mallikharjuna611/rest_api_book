from django.shortcuts import render
from TaskApp.models import Task
from TaskApp.serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer



class DueTaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')\
                            .filter(completed=False)
    serializer_class = TaskSerializer
    


class CompletedTaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created')\
                            .filter(completed=True)
    serializer_class = TaskSerializer

