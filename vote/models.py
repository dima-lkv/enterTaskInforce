from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from menu.models import Menu


# Create your models here.
class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=10, default=datetime.now().strftime("%m/%d/%Y"))
