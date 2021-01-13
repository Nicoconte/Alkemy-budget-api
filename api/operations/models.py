from django.db import models
from django.contrib.auth.models import User

class Operation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concept = models.CharField(max_length=1500)
    money_amount = models.FloatField()
    date = models.DateField()
    type = models.CharField(max_length=20)


    def __str__(self):
        return f"ID {self.id} | Usuario: {self.user.username} | Dinero: {self.money_amount} | Tipo: {self.type} | Fecha {self.date}"