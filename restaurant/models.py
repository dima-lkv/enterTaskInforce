import datetime

from django.db import models


# Create your models here.
class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    menu = models.TextField(blank=True)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=datetime.datetime.now(), editable=False)
