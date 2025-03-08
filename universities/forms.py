from django import forms

MATERIE_PREFERATA =(
    ("matematica", "Matematică"),
    ("informatica", "Informatică"),
    ("romana", "Română"),
    ("fizica", "Fizică")
)

LOCATIE_PREFERATA =(
    ("Bucuresti", "București"),
    ("Cluj", "Cluj"),
)

class Chestionar(forms.Form):
    materii_preferate = forms.MultipleChoiceField(
        label = "Ce materie îți place?",
        choices = MATERIE_PREFERATA,
        widget = forms.CheckboxSelectMultiple,
    )

    locatii_preferate = forms.MultipleChoiceField(
        label = "În ce orașe vrei să studiezi?",
        choices= LOCATIE_PREFERATA,
        widget=forms.CheckboxSelectMultiple
    )
    