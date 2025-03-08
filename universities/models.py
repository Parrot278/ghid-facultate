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

class Facultate(models.Model):
    nume = models.CharField(max_length = 255)
    descriere = models.TextField()
    rating = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    oameni_pe_loc = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    adresa = models.CharField(max_length = 255, blank=True)
    oras = models.CharField(max_length = 200, blank=True)
    programe = models.ManyToManyField(Program, blank=True)
    
    def __str__(self):
        return self.nume
    class Meta:
        verbose_name_plural = "facultati"
    

# class Intrebare(models.Model):
#     text_intrebare = models.TextField()

#     def __str__(self): # cand se apeleaza .self ne arata textul intrebarii
#         return self.text_intrebare
#     class Meta:
#         verbose_name_plural = "intrebari"


# class Raspuns(models.Model):
#     intrebare = models.ForeignKey(Intrebare, on_delete = models.CASCADE)
#     text_raspuns = models.CharField(max_length=200)

#     def __str__(self):
#         return self.text_raspuns
#     class Meta:
#         verbose_name_plural = "raspunsuri"



