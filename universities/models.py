from django.db import models

# Create your models here.

class Facultate(models.Model):
    nume = models.CharField(max_length = 255)
    descriere = models.TextField()
    rating = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    oameni_pe_loc = models.DecimalField(max_digits = 3, decimal_places=1, default= 0.0)
    locatie = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "facultati"
    

class Intrebare(models.Model):
    text_intrebare = models.TextField()

    def __str__(self): # cand se apeleaza .self ne arata textul
        return self.text_intrebare
    
    class Meta:
        verbose_name_plural = "intrebari"


class Raspuns(models.Model):
    intrebare = models.ForeignKey(Intrebare, on_delete = models.CASCADE)
    text_raspuns = models.CharField(max_length=200)

    def __str__(self):
        return self.text_raspuns
    
    class Meta:
        verbose_name_plural = "raspunsuri"



