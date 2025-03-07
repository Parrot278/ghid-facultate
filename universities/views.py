from django.shortcuts import render, get_object_or_404
from django.db import connection
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
    return render(request, "universities/detaliifacultate.html", {"facultate": facultate})

def chestionar(request):
    if request.method == "POST":
        form = Chestionar(request.POST)
        if form.is_valid():
            materie = form.cleaned_data["materie_preferata"]

            with connection.cursor() as cursor:
                placeholders = ', '.join(['%s'] * len(materie))
                query = f"""
                    SELECT * FROM universities_facultate WHERE id IN (
                        SELECT DISTINCT facultate_id FROM universities_facultate_programe WHERE program_id IN (
                            SELECT program_id FROM universities_program_materii 
                            WHERE materie_id IN (SELECT id FROM universities_materie WHERE nume IN ({placeholders}))
                        )
                    )
                """
                cursor.execute(query, materie)
                rez = cursor.fetchall()

                
            
            return render(request, "universities/rezultatechestionar.html", {
                "materie": materie,
                "rezultate": rez,
            })
    else:
        form = Chestionar()
    
    return render(request, "universities/chestionar.html", {"form": form})
