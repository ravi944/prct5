from django.db import models


class test(models.Model):
    name = models.CharField(max_length=200)
    Position = models.CharField(max_length=200)
    Office = models.CharField(max_length=200)
    Age = models.IntegerField()
    startdate = models.DateField()
    salary = models.IntegerField()
