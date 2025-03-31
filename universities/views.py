from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import Chestionar, ContactForm
from .models import Facultate
from .forms import FeedbackForm
from .models import Feedback
from django.views.generic import ListView

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
            rezultate_facultati = Facultate.objects.all()

            #1 PASIUNI
            pasiuni = form.cleaned_data.get("pasiuni", [])
            if pasiuni:
                rezultate_facultati = rezultate_facultati.filter(pasiuni__nume__in = pasiuni).distinct()
            
            #2 MATERII
            materii_preferate = form.cleaned_data.get("materii_preferate", [])
            if materii_preferate:
                rezultate_facultati = rezultate_facultati.filter(programe__materii__nume__in = materii_preferate).distinct()

            #3 SKILLURI
            skilluri = form.cleaned_data.get("skilluri", [])
            if skilluri:
                rezultate_facultati = rezultate_facultati.filter(skilluri__nume__in = skilluri).distinct()

            #4 TIMP PREGATIRE
            timp_pregatire = form.cleaned_data.get("timp_pregatire", [])
            if timp_pregatire:
                rezultate_facultati = rezultate_facultati.filter(timp_necesar__nume__in = timp_pregatire).distinct()

            #5 DOSAR
            dosar = form.cleaned_data.get("dosar", [])
            if dosar:
                rezultate_facultati = rezultate_facultati.filter(complexitate_dosar__nume__in = dosar).distinct()

            #6 DOMENII
            domenii_preferate = form.cleaned_data.get("domenii", [])
            if domenii_preferate:
                rezultate_facultati = rezultate_facultati.filter(domenii__nume__in = domenii_preferate).distinct()

            # ASTEA SUNT CELE REQUIRED
            
            #7 LOCATII PREFERATE
            locatii_preferate = form.cleaned_data["locatii_preferate"]
            rezultate_facultati = rezultate_facultati.filter(oras__in=locatii_preferate).distinct()

            #8 BUGET
            bugete_alese = form.cleaned_data.get("buget", [])
            BUGET_MAP = {
                "sub_1000": 1000 * 5,
                "1000_2000": 2000 * 5,
                "3000_4000": 4000 * 5,
                "5000_6000": 6000 * 5,
                "7000_8000": 8000 * 5,
                "10000_plus": 10000 * 5,
            }
            
            if bugete_alese:
                buget_maxim = max([BUGET_MAP[buget] for buget in bugete_alese if buget in BUGET_MAP], default=None)
                if buget_maxim is not None:
                    rezultate_facultati = rezultate_facultati.filter(buget_taxa__lte=buget_maxim).distinct()

            #9 E CU ADMITERE (EXAMEN)
            tip_admitere = form.cleaned_data.get("admitere", None)
            if tip_admitere:
                if tip_admitere == "dosar":
                    rezultate_facultati = rezultate_facultati.filter(cu_admitere=False).distinct()
                elif tip_admitere == "examen":
                    rezultate_facultati = rezultate_facultati.filter(cu_admitere=True).distinct()

            #10 E CU CAMIN
            camin_necesar = form.cleaned_data.get("camin_necesar", None)
            if camin_necesar == "necesar":
                rezultate_facultati = rezultate_facultati.filter(cu_camin=True).distinct()
            
            
            return render(request, "universities/rezultatechestionar.html", {
                "facultati": rezultate_facultati
            })
    else:
        form = Chestionar()
    
    return render(request, "universities/chestionar.html", {"form": form})




