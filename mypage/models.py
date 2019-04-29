from django.db import models

class Introduce(models.Model):
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    job = models.TextField()
    intro = models.TextField()
