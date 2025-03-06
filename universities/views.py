from django.shortcuts import render, get_object_or_404
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

def detalii_facultate(request, facultate_id):
    facultate = get_object_or_404(Facultate, id = facultate_id)
    return render(request, "universities/detaliifacultate.html"), {"facultate": facultate}

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
