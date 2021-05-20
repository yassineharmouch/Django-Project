# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Enfant(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    date = models.DateField('%m/%d/%Y')
    etat = models.CharField(max_length=40, blank=True)
    sante = models.CharField(max_length=40, blank=True)
    profession = models.CharField(max_length=40, blank=True)
    revenu = models.FloatField(default=0.0)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Pere(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    etat = models.CharField(max_length=40, blank=True)
    sante = models.CharField(max_length=40, blank=True)
    profession = models.CharField(max_length=40, blank=True)
    revenu = models.FloatField(default=0.0)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Mere(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    etat = models.CharField(max_length=40, blank=True)
    sante = models.CharField(max_length=40, blank=True)
    profession = models.CharField(max_length=40, blank=True)
    revenu = models.FloatField(default=0.0)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')



class Famille(models.Model):
    firstname1 = models.CharField(max_length=40, blank=False)
    lastname1 = models.CharField(max_length=40, blank=False)
    etat1 = models.CharField(max_length=40, blank=True)
    sante1 = models.CharField(max_length=40, blank=True)
    profession1 = models.CharField(max_length=40, blank=True)
    revenu1 = models.FloatField(default=0.0)
    firstname2 = models.CharField(max_length=40, blank=False)
    lastname2 = models.CharField(max_length=40, blank=False)
    etat2 = models.CharField(max_length=40, blank=True)
    sante2 = models.CharField(max_length=40, blank=True)
    profession2 = models.CharField(max_length=40, blank=True)
    revenu2 = models.FloatField(default=0.0)

    enfant = models.ForeignKey(Enfant, on_delete=models.CASCADE)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')


class Member(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    location = models.TextField(max_length=255, blank=False)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Ajax(models.Model):
    text = models.CharField(max_length=255, blank=True)
    search = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    end_date = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)




class Mere(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    etat = models.CharField(max_length=40, blank=True)
    sante = models.CharField(max_length=40, blank=True)
    profession = models.CharField(max_length=40, blank=True)
    revenu = models.FloatField(default=0.0)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Coordonnées(models.Model):
    adresse = models.CharField(max_length=255, blank=True)
    mobile_number = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Membere(models.Model):
    code_famille = models.CharField(max_length=40, blank=False)
    member = models.CharField(max_length=40, blank=False)
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    etat = models.CharField(max_length=40, blank=True)
    sante = models.CharField(max_length=40, blank=True)
    profession = models.CharField(max_length=40, blank=True)
    revenu = models.FloatField(default=0.0)
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

