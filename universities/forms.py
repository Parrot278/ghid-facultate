from django import forms

MATERIE_PREFERATA =(
    ("matematica", "Matematică"),
    ("informatica", "Informatică"),
    ("romana", "Română"),
)

class Chestionar(forms.Form):
    materie_preferata = forms.MultipleChoiceField(
        label = "Ce materie îți place?",
        choices = MATERIE_PREFERATA,
        widget = forms.RadioSelect,
    )