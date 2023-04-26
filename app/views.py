from django.shortcuts import render, redirect
from .models import Person, Employee
from .forms import PersonForm


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