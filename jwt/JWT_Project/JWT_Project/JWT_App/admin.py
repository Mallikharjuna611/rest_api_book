
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['empid','empname','salary','location']

admin.site.register(Employee,EmployeeAdmin)

