from __future__ import unicode_literals
from django.db import models

# Create your models here.
# Inside models.py

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.name, self.city, self.state)
class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojos = models.ForeignKey(Dojos, related_name = "ninjas")
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.dojos)