from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from TaskApp.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_name' , 'task_desc' , 'completed' ,
                  'date_created', 'image','doc']