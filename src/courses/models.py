from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=120)
