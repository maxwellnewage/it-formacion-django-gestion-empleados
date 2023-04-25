from django.shortcuts import render
from .models import Person


def home(request):
    persons = Person.objects.all()

    return render(request, 'home.html', {
        'persons': persons
    })


def about_us(request):
    return render(request, 'about_us.html')

