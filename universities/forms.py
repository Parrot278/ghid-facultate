from django import forms
from django.core.validators import EmailValidator

PASIUNI =(
    ("desen", "Desen"),
    ("muzica", "Muzică"),
    ("sport", "Sport"),
    ("proza_poezie", "Compunere de proză și poezie"),
    ("limbi_straine", "Limbi străine"),
    ("politica", "Politică"),
    ("voluntariat", "Voluntariat"),
    ("organizare_evenimente", "Organizare de evenimente"),
    ("public_speaking", "Public speaking"),
    ("it", "IT/programare"),
    ("animale", "Îngrijire/dresare de animale"),
    ("corp_uman", "Studiul corpului uman"),
    ("teatru", "Teatru, actorie"),
)

MATERIE_PREFERATA =(
    ("matematica", "Matematică"),
    ("romana", "Română"),
    ("engleza", "Engleză"),
    ("informatica", "Informatică"),
    ("fizica", "Fizică"),
    ("chimie", "Chimie"),
    ("biologie", "Biologie"),
    ("economie", "Economie"),
    ("istorie", "Istorie"),
    ("geografie", "Geografie"),
    ("religie", "Religie"),
    ("logica", "Logică"),
    ("sociologie", "Sociologie"),
    ("filosofie", "Filosofie"),
    ("sport", "Sport"),
    ("limbi_straine", "Limbi străine (franceză, germană, spaniolă, etc)"),
    ("psihologie", "Psihologie"),
)

SKILLS =(
    ("public_speaking", "Public speaking"),
    ("leadership", "Leadership"),
    ("talent_artistic", "Talent artistic: muzică, desen, teatru, etc"),
    ("lucrez_echipa", "Lucrez bine în echipă"),
    ("lucrez_singur", "Lucrez bine de unul singur"),
    ("time_management", "Time management eficient"),
    ("gestionare_oameni", "Gestionarea oamenilor într-un anumit context"),
    ("programare", "Mă descurc la programare"),
    ("design_digital", "Mă pricep la design digital"),
)

TIMP_PREGATIRE =(
    ("1_2_luni", "1-2 luni"),
    ("3_6_luni", "3-6 luni"),
    ("6_12_luni", "6 luni - 1 an"),
    ("1_2_ani", "1-2 ani"),
    ("2_plus_ani", "2+ ani"),
)

DOSAR =(
    ("complet", "Da, am un dosar complex, cu voluntariate, concursuri și/sau certificate"),
    ("voluntariate", "Da, doar cu voluntariate și activități extracurriculare"),
    ("concursuri", "Da, doar cu concursuri și/sau certificate"),
    ("mixt", "Da, cu câteva activități și certificări din fiecare"),
    ("in_pregatire", "Este în pregătire și va îndeplini toate criteriile"),
    ("insuficient", "Am un dosar, dar nu este suficient de complex"),
    ("nu", "Nu am un dosar"),
)

LOCATIE_PREFERATA =(
    ("Bucuresti", "București"),
    ("Cluj", "Cluj"),
)

class Chestionar(forms.Form):

    pasiuni = forms.MultipleChoiceField(
        label = "Ce pasiuni ai?",
        choices = PASIUNI,
        widget= forms.CheckboxSelectMultiple,
    )

    materii_preferate = forms.MultipleChoiceField(
        label = "Ce materie îți place?",
        choices = MATERIE_PREFERATA,
        widget = forms.CheckboxSelectMultiple,
    )

    materii_preferate = forms.MultipleChoiceField(
        label = "Ce skilluri ai?",
        choices = SKILLS,
        widget = forms.CheckboxSelectMultiple,
    )

    locatii_preferate = forms.MultipleChoiceField(
        label = "În ce orașe vrei să studiezi?",
        choices= LOCATIE_PREFERATA,
        widget=forms.CheckboxSelectMultiple
    )


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)