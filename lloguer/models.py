from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.marca} {self.model} {self.matricula}"

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensures each vote is linked to a user
    cotxe = models.ForeignKey(Automobil, on_delete=models.CASCADE, related_name="vots")
    data_inici = models.DateField()
    data_final = models.DateField(blank=True,null=True)

    class Meta:
        unique_together = ('cotxe', 'data_inici')  # Ensures a user can only vote once per option

    def __str__(self):
        return f"[{self.data_inici}] {self.user.username} → {self.cotxe.marca} {self.cotxe.model} {self.cotxe.matricula}"