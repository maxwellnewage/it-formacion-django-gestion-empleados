from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm


def home(request):
    persons = Person.objects.all()

    return render(request, 'home.html', {
        'persons': persons
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
            form.save()
            return redirect('home')

    return render(request, 'form.html', {
        'form': form,
        'submit': 'Crear',
        'title': 'Crear Persona',
        'action': 'btn-primary'
    })
