from django.db import models
from accounts.models import Profile

class Rendezvous(models.Model):
    date = models.DateTimeField()
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rendezvous_as_client')
    doctor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rendezvous_as_doctor')
    etat = models.BooleanField(default=False)  # False signifie que le rendez-vous n'est pas encore accepté
    note = models.TextField() ; 
    def __str__(self):
        return f"Rendezvous with {self.client.email} at {self.date}"
