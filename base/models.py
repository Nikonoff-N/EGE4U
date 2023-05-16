from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    master = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField("date published")
    number = models.IntegerField()
    state = models.BooleanField()
