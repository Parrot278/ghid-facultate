from django.db import models
from django.utils import timezone

# Create your models here.
class ParticipareOlimpiade(models.Model):
    tip_participare = models.CharField(max_length = 150)
    def __str__(self):
        return self.tip_participare
    class Meta:
        verbose_name_plural = "participari_olimpiade"

class Materie(models.Model):
    nume = models.CharField(max_length = 150)
    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "materii"

class Program(models.Model):
    nume = models.CharField(max_length = 100)
    tip = models.CharField(max_length = 100)
    materii = models.ManyToManyField(Materie)

    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "programe"

class Domeniu(models.Model):
    nume = models.CharField(max_length = 100)

    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "domenii"

class Skill(models.Model):
    nume = models.CharField(max_length = 100)

    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "skills"

class TimpNecesar(models.Model):
    nume = models.CharField(max_length=100)
    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "timp_necesar"

class ComplexitateDosar(models.Model):
    nume = models.CharField(max_length=100)
    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "complexitate_dosar"

class Pasiune(models.Model):
    nume = models.CharField(max_length=100)
    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "pasiuni"

class Facultate(models.Model):
    nume = models.CharField(max_length = 255)
    descriere = models.TextField()
    rating = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    oameni_pe_loc = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    adresa = models.CharField(max_length = 255, blank=True)
    oras = models.CharField(max_length = 200, blank=True)
    buget_taxa = models.DecimalField(max_digits = 6, decimal_places=0, default = 0, blank = True)
    buget_camin = models.DecimalField(max_digits = 6, decimal_places=0, default = 0, blank = True)
    cu_camin = models.BooleanField(default = False)
    cu_admitere = models.BooleanField(default = False)

    pasiuni = models.ManyToManyField(Pasiune, blank = True)
    programe = models.ManyToManyField(Program, blank=True)
    domenii = models.ManyToManyField(Domeniu, blank=True)
    skilluri = models.ManyToManyField(Skill, blank=True)
    timp_necesar = models.ManyToManyField(TimpNecesar, blank = True)
    complexitate_dosar = models.ManyToManyField(ComplexitateDosar, blank = True)
    participare_olimpiade = models.ManyToManyField(ParticipareOlimpiade, blank = True)
    
    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "facultati"
    
class Feedback(models.Model):
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Below Average'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    )
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Feedback from {self.name} ({self.rating}/5)"
    
    class Meta:
        ordering = ['-created_at']


