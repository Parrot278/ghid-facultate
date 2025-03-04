from django.contrib import admin
from . models import Facultate, Intrebare, Raspuns, Materie

# Register your models here.

admin.site.register(Facultate)
admin.site.register(Intrebare)
admin.site.register(Raspuns)
admin.site.register(Materie)