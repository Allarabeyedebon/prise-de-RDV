from random import random
import random
import string
import secrets
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.forms import FloatField
from django.utils.text import slugify
import os
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators

from requests import request

def random_string(num):
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
    return str(res)






# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    def save_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(('The given email must be set'))
        email = self.normalize_email(email)
        user  = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields['is_superuser'] = False
        extra_fields['is_staff'] = False
        return self.save_user(email, password, **extra_fields)

     

    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_superuser', True)
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError(_('is_superuser should be True'))
    #     extra_fields['is_staff'] = True
    #     return self.save_user(email, password, **extra_fields) 

        
   

    def __str__(self):
        return self.email



  
class Client(models.Model):

    class TypeCompte(models.TextChoices):
        EPARGNE = 'Epargne'
        COURANT = 'Courant'
        AUTRES = 'Autres'

    class Sexe(models.TextChoices):
        MASCULIN = 'Masculin'
        FEMININ = 'Feminin'
        AUTRES = 'Autres'

    nom               = models.CharField(max_length=250, blank=False, null=False)
    prenom            = models.CharField(max_length=250, blank=False, null=False)
    email             = models.EmailField('Email Adress', max_length=120)
    mote_de_passe      = models.CharField(max_length=250, blank=False, null=False)
    sexe              = models.CharField(max_length=20, choices=Sexe.choices, default = Sexe.MASCULIN)
    numero_Compte      = models.CharField(max_length=250, blank=False, null=False)
    Adresse           = models.CharField(max_length=250, blank=False, null=False)
    typeCompte        = models.CharField(max_length=20, default=TypeCompte.COURANT, choices = TypeCompte.choices)
    fonction          = models.CharField(max_length=250, blank=False, null=False)
    numeroTelephone   = models.CharField(max_length=250, blank=True, null=True)
    is_staff          = models.BooleanField(default=False)
    Adresse           = models.CharField(max_length=250, blank=True, null=True)
    dateAjout         = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModif         = models.DateTimeField(auto_now=True, auto_now_add=False)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    
  
    def __str__(self):
        return self.nom
    
    
JOUR = (
    ('Lundi','Lundi'),
    ('Mardi','Mardi'),
    ('Mercredi','Mercredi'),
    ('Jeudi','Jeudi'),
    ('Vendredi','Vendredi'),
    ('Samedi','Samedi'),
    ('Dimanche','Dimanche'),
)


HEUREF = (
    ('15H30','15H30'),
    ('11H30','11H30'),
)
HEUREO = (
    ('08H30','08H30'),
)


class Agence(models.Model):
    nom               = models.CharField(max_length=250, blank=False, null=False)
    Ville             = models.CharField(max_length=250, blank=False, null=False)
    local             = models.CharField(max_length=250, blank=False, null=False)
    heureOuverture    = models.CharField(max_length=200, choices = HEUREO, default='08H30',  blank=False, null=False)
    heureFermeture    = models.CharField(max_length=200, choices = HEUREF, blank=False, null=False)
    dateAjout          = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModif          = models.DateTimeField(auto_now=True, auto_now_add=False)
    photo              = models.ImageField(upload_to='images', blank=True, null=True) 

    def __str__(self):
        return self.nom 



class Service(models.Model):
    nom               = models.CharField(max_length=250, blank=False, null=False)
    agence             = models.ManyToManyField(Agence, blank=True, related_name='user_com')
    description             = models.CharField(max_length=250, blank=False, null=False)
    dateAjout          = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModif          = models.DateTimeField(auto_now=True, auto_now_add=False)
    photo              = models.ImageField(upload_to='images', blank=True, null=True) 

    def __str__(self):
        return self.nom 


 
 
    
class Gestionnaire(models.Model):

    class Sexe(models.TextChoices):
          MASCULIN = 'Masculin'
          FEMININ = 'Feminin'
          AUTRES = 'Autres'

    nom              = models.CharField(max_length=250, blank=False, null=False)
    prenom           = models.CharField(max_length=250, blank=False, null=False)
    agence            = models.ForeignKey(Agence , on_delete=models.CASCADE, blank=False, null=False)
    sexe              = models.CharField(max_length=20, choices=Sexe.choices, default = Sexe.MASCULIN)
    Adresse           = models.CharField(max_length=250, blank=False, null=False)
    email             = models.EmailField(max_length=250, blank=True, null=True)
    numeroTelephone   = models.CharField(max_length=250, blank=True, null=True)
    disponibilite     = models.BooleanField(default=True)
    dateAjout         = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModif         = models.DateTimeField(auto_now=True, auto_now_add=False)
    photo             = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.nom 





TYPEPROBLEME = (
    ('Compte Bloqué','Compte Bloqué'),
    ('Autres','Autres'),
)


TEMPS = (
    ('08H45-09H00','08H45-09H00'),
    ('11H00-11H15','11H00-11H45'),
    ('12H30-12H45','12H30-12H45'),
)


class RDV(models.Model):
    client             = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    gestionnaire       = models.ForeignKey(Gestionnaire, on_delete=models.CASCADE, blank=False, null=False)
    typeProbleme       = models.CharField(max_length=200, choices = TYPEPROBLEME, blank=False, null=False)
    horaire            = models.CharField(max_length=200, choices = TEMPS,  blank=False, null=False)
    description        = models.TextField(max_length=200)
    dateAjout          = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateModif          = models.DateTimeField(auto_now=True, auto_now_add=False)
   

    def __str__(self):
        return self.client.nom 
