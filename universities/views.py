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
            
            
            rezultate_facultati = Facultate.objects.all()

            #1 Stii domeniul

            #2 PASIUNI
            pasiuni = form.cleaned_data["pasiuni"]
            rezultate_facultati = rezultate_facultati.filter(pasiuni__nume__in = pasiuni).distinct()
            
            #3 MATERII
            materii_preferate = form.cleaned_data["materii_preferate"]
            rezultate_facultati = rezultate_facultati.filter(programe__materii__nume__in = materii_preferate).distinct()

            #4 SKILLURI
            skilluri = form.cleaned_data["skilluri"]
            rezultate_facultati = rezultate_facultati.filter(skilluri__nume__in = skilluri).distinct()

            #5 TIMP PREGATIRE
            timp_pregatire = form.cleaned_data["timp_pregatire"]
            rezultate_facultati = rezultate_facultati.filter(timp_necesar__nume__in = timp_pregatire).distinct()

            #6 DOSAR
            dosar = form.cleaned_data["dosar"]
            rezultate_facultati = rezultate_facultati.filter(complexitate_dosar__nume__in = dosar).distinct()

            #7 OLIMPIADE
            olimpiade = form.cleaned_data["olimpiade"]
            rezultate_facultati = rezultate_facultati.filter(participare_olimpiade__tip_participare__in = olimpiade).distinct()

            #8 DOMENII
            domenii_preferate = form.cleaned_data["domenii"]
            rezultate_facultati = rezultate_facultati.filter(domenii__nume__in = domenii_preferate).distinct()

            #9 LOCATII PREFERATE
            locatii_preferate = form.cleaned_data["locatii_preferate"]
            rezultate_facultati = rezultate_facultati.filter(oras__in=locatii_preferate).distinct()

            #10 BUGET
            bugete_alese = form.cleaned_data["buget"]
            BUGET_MAP = {
                "sub_1000": 1000,
                "1000_2000": 2000,
                "3000_4000": 4000,
                "5000_6000": 6000,
                "7000_8000": 8000,
                "10000_plus": 10000,
            }
            
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
                if buget in BUGET_MAP:
                    buget_numeric = BUGET_MAP[buget]
                    buget_minim, buget_maxim = RANGES_BUGET[buget_numeric]
                    
                    if buget_maxim == float("inf"):  
                        query_buget |= Q(buget_taxa__gte=buget_minim)
                    else:
                        query_buget |= Q(buget_taxa__gte=buget_minim, buget_taxa__lte=buget_maxim)
            
            rezultate_facultati = rezultate_facultati.filter(query_buget).distinct()

            #11 E CU ADMITERE (EXAMEN)
            tip_admitere = form.cleaned_data["admitere"]
            if tip_admitere == "dosar":
                rezultate_facultati = rezultate_facultati.filter(cu_admitere=False).distinct()
            elif tip_admitere == "examen":
                rezultate_facultati = rezultate_facultati.filter(cu_admitere=True).distinct()

            #12 E CU CAMIN
            camin_necesar = form.cleaned_data["camin_necesar"]
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