from django.forms import ModelForm
from .models import Person, Employee


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ('is_active',)


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
