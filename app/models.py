from django.db import models
from django.contrib.auth.models import User

class Performer(models.Model):
  user = models.ForeignKey(User, unique=True)
  name = models.CharField(max_length=256)
  pic_url = models.CharField(max_length=4096)
  copy = models.CharField(max_length=4096)

class Judge(models.Model):
  name = models.CharField(max_length=256)
  user = models.ForeignKey(User, unique=True)

class Review(models.Model):
  performance = models.ForeignKey(Performance)
  judge = models.ForeignKey(Judge)
  notes = models.CharField(max_length=4096)
    
class Performance(models.Model):
  active = models.BooleanField(default=False)
  planned_time = models.DateTimeField()
  performers = models.ManyToManyField(Performer)

