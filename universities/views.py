from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import Chestionar, ContactForm
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
    return render(request, "universities/detaliifacultate.html", {"facultate": facultate})

def chestionar(request):
    if request.method == "POST":
        form = Chestionar(request.POST)
        if form.is_valid():
            materii_preferate = form.cleaned_data["materii_preferate"]
            locatii_preferate = form.cleaned_data["locatii_preferate"]

            rezultate_facultati = Facultate.objects.all()

            rezultate_facultati = rezultate_facultati.filter(programe__materii__nume__in=materii_preferate).distinct()
            rezultate_facultati = rezultate_facultati.filter(oras__in=locatii_preferate).distinct()

                
            
            return render(request, "universities/rezultatechestionar.html", {
                "materie": materii_preferate,
                "facultati": rezultate_facultati
            })
    else:
        form = Chestionar()
    
    return render(request, "universities/chestionar.html", {"form": form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Mesajul a fost trimis cu succes!")
            return render(request, "universities/bibliografie.html")
    
    else:
        form = ContactForm()
    return render(request, "universities/bibliografie.html", {"form": form})