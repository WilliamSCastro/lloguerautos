from django.shortcuts import render

# Create your views here.
from .models import Automobil  # Assegura't que el model existeix

def veure_autos(request):
    autos = Automobil.objects.all()
    return render(request, 'llista_autos.html', {'automobils': autos})
    # render, template a cargar, datos que se pasan