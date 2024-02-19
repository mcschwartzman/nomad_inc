import datetime

from django.db import models

# Create your models here.

class Company(models.Model):

    name = models.CharField(max_length=200)
    incorporation_date = models.DateTimeField("date incorporated")

    def describe(self):
        
        return "{0}, {1}".format(self.name, self.incorporation_date.year)

    def __str__(self):

        return self.name

class Scorer(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    green_score = models.IntegerField(default=0)