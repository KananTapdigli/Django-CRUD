from django.db import models
from .tools import GENDER_CHOICES

class User(models.Model):
    name = models.CharField(max_length=50,verbose_name="Ad:",help_text="Ad daxil edin")
    surname = models.CharField(max_length=50, verbose_name="Soyad:", help_text="Soyad daxil edin")
    email = models.EmailField(max_length=50, verbose_name="Poçt ünvanı:", help_text="Poçt ünvanını daxil edin", unique=True)
    age = models.IntegerField(verbose_name="Yas:", help_text="Yas daxil edin")
    gender = models.IntegerField(choices=GENDER_CHOICES)

    def show_gender(self):
        if self.gender == 0:
            return "Kişi"
        elif self.gender == 1:
            return "Qadın"
