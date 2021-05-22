from django.db import models
from django.forms import ModelForm


# Create your models here.
class Register(models.Model):
    usernamename = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.name

class Registerbtn(models.Model):
    Requirement = models.CharField(max_length=50)
    Quantity = models.IntegerField() 

    def __str__(self):
        return self.Requirement 