# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
list_of_types_material = (('', ''),
                          ('', ''),
                          ('', ''),
                          ('', ''),
                          ('', ''),
                          ('', ''),
                          ('', ''))
list_month = {1: 'month',
              2: 'month',
              3: 'month',
              6: 'month',
              12: 'month'}


class Client(models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    CIN = models.CharField(max_length=60)
    Tel = models.IntegerField()
    Email = models.EmailField()
    Age = models.IntegerField()
    CreatedAt = models.DateField()
    Picture = models.FileField(upload_to="media")

    def __str__(self):
        return f'{self.FirstName} {self.LastName} '


class Salle(models.Model):
    Name = models.CharField(max_length=60)
    Localisation = models.CharField(max_length=255)
    IsOpen = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.Name} '


class Material(models.Model):
    Name = models.CharField(max_length=60)
    Type = models.CharField(max_length=60,choices=list_of_types_material)
    BuyDate = models.DateField()
    UseDate = models.DateField()
    Picture = models.FileField(upload_to="media")

    def __str__(self):
        return f'{self.Name} '


#   IdSalle = models.ForeignKey(Salle)


class Coach(models.Model):
    FirstName = models.CharField(max_length=60)
    LastName = models.CharField(max_length=60)
    CIN = models.CharField(max_length=60)
    Salary = models.IntegerField()
    IdSalle = models.ForeignKey(Salle, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.FirstName} {self.LastName} '


class Contact(models.Model):
    Name = models.CharField(max_length=60)
    Email = models.EmailField()
    Subject = models.CharField(max_length=255)
    Message = models.TextField()
    Seen = models.BooleanField()
    CreatedAt = models.DateField()

    def __str__(self):
        return f'{self.Name} '


class Discount(models.Model):
    Period = models.CharField(max_length=255)
    Percentage = models.IntegerField()

    def __str__(self):
        return f'{self.Period} {self.Percentage}'

"""
def getdiscount():
    discounts = get_list_or_404(Discount)
    return discounts
"""
#list = getdiscount()
class Subscription(models.Model):
    StartDate = models.DateField()
    Duration = models.CharField(max_length=60)
    EndSubscription = models.DateField()
    SubscriptionPrice = models.FloatField()
    ActiveInsurance = models.BooleanField()
    IdClient = models.ForeignKey(Client, on_delete=models.CASCADE)

