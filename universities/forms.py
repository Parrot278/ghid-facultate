from django import forms
from django.core.validators import EmailValidator


PASIUNI =(
    ("desen", "Desen"),
    ("muzica", "Muzică"),
    ("sport", "Sport"),
    ("proza_poezie", "Compunere de proză și poezie"),
    ("limbi_straine", "Limbi străine"),
    ("stiinte_sociale", "Științe sociale și umaniste"),
    ("politica", "Politică"),
    ("voluntariat", "Voluntariat"),
    ("organizare_evenimente", "Organizare de evenimente"),
    ("public_speaking", "Public speaking"),
    ("economie_antreprenoriat", "Economie și antreprenoriat"),
    ("it", "Dezvoltare software"),
    ("inginerie", "Inginerie"),
    ("stiinte_exacte", "Științe exacte"),
    ("animale", "Îngrijire/dresare de animale"),
    ("corp_uman", "Studiul corpului uman"),
    ("stiinte_ale_naturii", "Științe ale naturii"),
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
    ("Abilități tehnice excelente", "Talent muzical și abilități tehnice excelente"),
    ("Capacitate de lucru cu date mari și complexitate mare", "Capacitate de lucru cu date mari și complexitate mare"),
    ("Talent artistic: muzică, desen, teatru, etc", "Talent artistic: muzică, desen, teatru, etc"),
    ("Abilități de traducere și interpretariat", "Abilități de traducere și interpretariat"),
    ("Cunoștințe solide de biologie, chimie și fizică", "Cunoștințe solide de biologie, chimie și fizică"),
    ("Capacitate de argumentare logică", "Capacitate de argumentare logică"),
    ("Cunoștințe de economie, finanțe și marketing", "Cunoștințe de economie, finanțe și marketing"),
    ("Cunoștințe de programare", "Cunoștințe de programare"),
    ("Lucru sub presiune", "Lucru sub presiune"),
    ("Abilități de cercetare și laborator", "Abilități de cercetare și laborator"),
    ("Comunicare clară și persuasivă", "Comunicare clară și persuasivă"),
    ("Abilități sportive", "Abilități sportive"),
    ("Empatie față de oameni și animale", "Empatie față de oameni și animale"),
)

TIMP_PREGATIRE =(
    ("3 ani", "3 ani"),
    ("4 ani", "4 ani"),
    ("6 ani", "6 ani"),
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

DOMENII =(
    ("arhitectura", "Arhitectură, urbanism, design interior"),
    ("informatica", "Informatică, programare"),
    ("matematica", "Matematică"),
    ("cercetare", "Cercetare"),
    ("medicina", "Medicină"),
    ("farmaceutica", "Farmaceutică"),
    ("drept", "Drept"),
    ("psihologie", "Psihologie"),
    ("economice", "Economie și Finanțe"),
    ("teatru", "Teatru, actorie, cinematografie"),
    ("stiinte_politice", "Științe politice"),
    ("sociologie", "Sociologie"),
    ("invatamant", "Invățământ"),
    ("inginerie", "Inginerie"),
    ("turism", "Turism, hospitality"),
    ("arte", "Domenii artistice (muzică, desen)"),
    ("sport", "Sport"),

)


LOCATIE_PREFERATA =(
    ("Bucuresti", "București"),
    ("Cluj", "Cluj-Napoca"),
    ("Iasi", "Iași"),
    ("Timisoara", "Timișoara"),
    ("Constanta", "Constanța"),
    ("Sibiu", "Sibiu"),
    ("Brasov", "Brașov"),
    ("Oradea", "Oradea"),
)

BUGET = (
    ("sub_1000", "Sub 1000 euro"),
    ("1000_2000", "1000-2000 euro"),
    ("3000_4000", "3000-4000 euro"),
    ("5000_6000", "5000-6000 euro"),
    ("7000_8000", "7000-8000 euro"),
    ("10000_plus", "10.000+ euro"),
)

ADMITERE =(
    ("dosar", "Dosar"),
    ("examen", "Examen"),
    ("indiferent", "Îmi este indiferent")
)

CAMIN_NECESAR =(
    ("necesar", "Da"),
    ("nu_necesar", "Nu, îmi pot găsi singur cazare")
)


class Chestionar(forms.Form):

    stii_domeniul = forms.ChoiceField(
        label = "Știi sigur în ce domeniu dorești să studiezi? Dacă nu ești hotărât, te putem ajuta prin câteva intrebări!",
        choices = [
            ("da", "Da"),
            ("nu", "Nu"),
        ],
        widget = forms.RadioSelect,
        required=True,
    )
    
    pasiuni = forms.MultipleChoiceField(
        label = "Ce pasiuni ai?",
        choices = PASIUNI,
        widget= forms.CheckboxSelectMultiple,
        required=False,
    )

    materii_preferate = forms.MultipleChoiceField(
        label = "Ce materie îți place?",
        choices = MATERIE_PREFERATA,
        widget = forms.CheckboxSelectMultiple,
        required=False,
    )

    skilluri = forms.MultipleChoiceField(
        label = "Ce skilluri consideri că ai?",
        choices= SKILLS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    timp_pregatire = forms.MultipleChoiceField(
        label = "Cât de lungă ai prefera să fie durata studiilor universitare?",
        choices= TIMP_PREGATIRE,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    dosar = forms.MultipleChoiceField(
        label = "Ai un dosar bine realizat?",
        choices= DOSAR,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    domenii = forms.MultipleChoiceField(
        label = "În ce domeniu dorești să studiezi?",
        choices= DOMENII,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    locatii_preferate = forms.MultipleChoiceField(
        label = "În ce orașe ți-ai dori să studiezi?",
        choices= LOCATIE_PREFERATA,
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    buget = forms.MultipleChoiceField(
        label = "Bugetul alocat pentru taxa de școlarizare?",
        choices= BUGET,
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    admitere = forms.ChoiceField(
        label = "Dorești o facultate cu admitere pe baza de dosar sau examen?",
        choices= ADMITERE,
        widget=forms.RadioSelect,
        required=True,
    )

    camin_necesar = forms.ChoiceField(
        label="Este necesar ca facultatea să aibă cămin propriu?",
        choices= CAMIN_NECESAR,
        widget=forms.RadioSelect,
        required=True,
    )


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)

# INTREBARI NEFOLOSITE
# olimpiade = forms.MultipleChoiceField(
#         label = "Ai participat la concursuri școlare/olimpiade?",
#         choices= OLIMPIADE,
#         widget=forms.CheckboxSelectMultiple
#     )
# OLIMPIADE =(
#     ("scoala", "Etapa pe școală"),
#     ("municipiu", "Etapa pe municipiu"),
#     ("judeteana", "Etapa județeană"),
#     ("nationala", "Etapa națională, fără premiu"),
#     ("premiu_nationala", "Etapa națională, cu premiu"),
#     ("internationala", "Etapa internațională"),
#     ("altfel", "Etapele sunt clasificate altfel"),
#     ("nu", "Nu am participat"),
# )