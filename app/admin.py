from django.contrib import admin
from .models import Person, Employee


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'birth', 'height', 'is_active')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('person', 'salary', 'seniority')
