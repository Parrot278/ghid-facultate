from django.db import models
# Create your models here.

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
        verbose_name_plural = "domenii"

class Facultate(models.Model):
    nume = models.CharField(max_length = 255)
    descriere = models.TextField()
    rating = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    oameni_pe_loc = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    adresa = models.CharField(max_length = 255, blank=True)
    oras = models.CharField(max_length = 200, blank=True)
    buget_taxa = models.DecimalField(max_digits = 6, decimal_places=0, default = 0, blank = True)
    buget_camin = models.DecimalField(max_digits = 6, decimal_places=0, default = 0, blank = True)


    programe = models.ManyToManyField(Program, blank=True)
    domenii = models.ManyToManyField(Domeniu, blank=True)
    skilluri = models.ManyToManyField(Skill, blank=True)
    
    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "facultati"
    




