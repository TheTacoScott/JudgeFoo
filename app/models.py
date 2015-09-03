from django.db import models

class Performer(models.Model):
  first_name = models.CharField(max_length=256)
  last_name = models.CharField(max_length=256)
  nickname = models.CharField(max_length=256)
  pic_url = models.CharField(max_length=4096)
  copy = models.CharField(max_length=4096)

class Judge(models.Model):
  first_name = models.CharField(max_length=256)
  last_name = models.CharField(max_length=256)

class Review(models.Model):
  performance = models.ForeignKey(Performance)
  judge = models.ForeignKey(Judge)
  notes = models.CharField(max_length=4096)
    
class Performance(models.Model):
  active = models.BooleanField(default=False)
  planned_time = models.DateTimeField()
  performers = models.ManyToManyField(Performer)

