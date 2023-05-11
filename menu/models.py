from datetime import datetime

from django.db import models
from restaurant.models import Restaurant


# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    choice = models.TextField(blank=False)
    week_day = models.IntegerField(default=datetime.now().weekday())
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=10, default=datetime.now().strftime("%m/%d/%Y"))
