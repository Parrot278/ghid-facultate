from django.contrib import admin
from .models import Facultate, Materie, Program, Domeniu, Skill, TimpNecesar, ComplexitateDosar, Pasiune

# Register your models here.

admin.site.register(Facultate)
admin.site.register(Materie)
admin.site.register(Program)
admin.site.register(Domeniu)
admin.site.register(Skill)
admin.site.register(TimpNecesar)
admin.site.register(ComplexitateDosar)
admin.site.register(Pasiune)