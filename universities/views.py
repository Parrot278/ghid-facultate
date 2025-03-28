from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
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
            pasiuni = form.cleaned_data["pasiuni"]
            skilluri = form.cleaned_data["skilluri"]
            timp_pregatire = form.cleaned_data["timp_pregatire"]
            dosar = form.cleaned_data["dosar"]
            olimpiade = form.cleaned_data["olimpiade"]
            domenii_preferate = form.cleaned_data["domenii"]
            bugete_alese = [int(buget) for buget in bugete_alese] 
            tip_admitere = form.cleaned_data["admitere"]
            camin_necesar = form.cleaned_data["camin_necesar"]

            rezultate_facultati = Facultate.objects.all()

            #1 Stii domeniul

            #2 PASIUNI
            rezultate_facultati = rezultate_facultati.filter(pasiuni__nume__in = pasiuni).distinct()
            
            #3 MATERII
            rezultate_facultati = rezultate_facultati.filter(programe__materii__nume__in = materii_preferate).distinct()

            #4 SKILLURI
            rezultate_facultati = rezultate_facultati.filter(skilluri__nume__in = skilluri).distinct()

            #5 TIMP PREGATIRE
            rezultate_facultati = rezultate_facultati.filter(timp_necesar__nume__in = timp_pregatire).distinct()

            #6 DOSAR
            rezultate_facultati = rezultate_facultati.filter(complexitate_dosar__nume__in = dosar).distinct()

            #7 OLIMPIADE
            rezultate_facultati = rezultate_facultati.filter(participare_olimpiade__tip_participare__in = olimpiade).distinct()

            #8 DOMENII
            rezultate_facultati = rezultate_facultati.filter(domenii__nume__in = domenii_preferate).distinct()

            #9 LOCATII PREFERATE
            rezultate_facultati = rezultate_facultati.filter(oras__in=locatii_preferate).distinct()

            #10 BUGET
            RANGES_BUGET = {
                1000: (0, 1000),
                2000: (1000, 2000),
                4000: (3000, 4000),
                6000: (5000, 6000),
                8000: (7000, 8000),
                10000: (10000, float("inf")),
            }
            query_buget = Q()
            for buget in bugete_alese:
                buget_minim, buget_maxim = RANGES_BUGET[buget]

                if buget_maxim == float("inf"):  
                    query_buget |= Q(budget__gte=buget_minim)
                else:
                    query_buget |= Q(budget__gte=buget_minim, budget__lte=buget_maxim)
            
            rezultate_facultati = rezultate_facultati.filter(query_buget).distinct()

            #11 E CU ADMITERE (EXAMEN)
            if tip_admitere == "dosar":
                rezultate_facultati = rezultate_facultati.filter(cu_admitere=False).distinct()
            elif tip_admitere == "examen":
                rezultate_facultati = rezultate_facultati.filter(cu_admitere=True).distinct()

            #12 E CU CAMIN
            if camin_necesar == "necesar":
                rezultate_facultati = rezultate_facultati.filter(cu_camin = True).distinct()
            
            

            
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