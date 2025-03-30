from django.contrib import admin
from .models import Facultate, Materie, Program, Domeniu, Skill, TimpNecesar, ComplexitateDosar, Pasiune, ParticipareOlimpiade, Feedback

# Register your models here.

admin.site.register(Facultate)
admin.site.register(Materie)
admin.site.register(Program)
admin.site.register(Domeniu)
admin.site.register(Skill)
admin.site.register(TimpNecesar)
admin.site.register(ComplexitateDosar)
admin.site.register(Pasiune)
admin.site.register(ParticipareOlimpiade)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)