from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Chestionar
from .models import Facultate

# Create your views here.

def ecran_principal(request):
    return render(request, "universities/ecran.principal.html")

def facultati_romania(request):
    return render(request, "universities/facultati.romania.html")

def catalog_facultati(request):
    items = Facultate.objects.all()
    return render(request, "universities/catalogfacultati.html", {"facultati": items} )

def cv_meniu(request):
    return render(request, "universities/cv.de.succes.html")

def bibliografie(request):
    return render(request, "universities/bibliografie.html")

def chestionar(request):
    if request.method == "POST":
        form = Chestionar(request.POST)
        if form.is_valid():
            materie = form.cleaned_data["materie_preferata"]

            rezultate_facultati = Facultate.objects.filter(
                materie__in = Facultate.materii
            )
            return render(request, "universities/rezultate_chestionar.html", {
                "materie": materie,
                "facultati": rezultate_facultati
            })
        else:
            form = Chestionar()
    
    return render(request, "universities/chestionar.html", {"form": form})
