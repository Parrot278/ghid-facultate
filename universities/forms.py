from django import forms
from django.core.validators import EmailValidator

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


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)