from django.shortcuts import render, redirect
from django.http import HttpResponse
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

def chestionar(request):
    return render(request, "universities/chestionar.html")

def bibliografie(request):
    return render(request, "universities/bibliografie.html")

def salvare_raspunsuri_sesiune(request):
    if request.method == "POST":
        if "raspunsuri_chestionar" not in request.session:
            request.session["raspunsuri_chestionar"] = {}
    
    for key, value in request.POST.items():
        if key.startswith("intrebare_"):
            request.session["raspunsuri_chestionar"][key] = value
        
        request.session.modified = True

        return redirect("")