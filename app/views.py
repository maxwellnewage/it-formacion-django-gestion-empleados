from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Person, Employee
from .forms import PersonForm, EmployeeForm
from django.contrib import messages
from django.http import JsonResponse


def home(request):
    persons = Person.objects.all()
    employees = Employee.objects.all()

    return render(request, 'home.html', {
        'persons': persons,
        'employees': employees
    })


def about_us(request):
    return render(request, 'about_us.html')


def delete_person(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    return redirect('home')


def create_person(request):
    form = PersonForm()

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.is_active = False
            person.save()
            return redirect('home')

    return render(request, 'form.html', {
        'form': form,
        'submit': 'Crear',
        'title': 'Crear Persona',
        'action': 'btn-primary'
    })


def update_person(request, person_id):
    person = Person.objects.get(id=person_id)
    form = PersonForm(instance=person)

    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'form.html', {
        'form': form,
        'submit': 'Modificar',
        'title': 'Modificar Persona',
        'action': 'btn-warning'
    })


def create_employee(request):
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            if empleado.person.is_active:
                empleado.save()
                return redirect('home')
            else:
                messages.error(request, "La persona no esta activa!")

    return render(request, 'form.html', {
        'form': form,
        'submit': 'Crear',
        'title': 'Crear Empleado',
        'action': 'btn-primary'
    })


def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()

    return redirect('home')
