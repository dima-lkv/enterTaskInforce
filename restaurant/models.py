from datetime import datetime

from django.db import models


# Create your models here.
class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    created_at = models.CharField(max_length=10, default=datetime.now().strftime("%m/%d/%Y"))
