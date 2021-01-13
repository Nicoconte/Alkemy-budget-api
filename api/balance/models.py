from django.db import models
from django.contrib.auth.models import User


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_money = models.FloatField(default=0.0) 

    def __str__(self):
        return f"Usuario: {self.user.username} | Dinero: {self.total_money}"