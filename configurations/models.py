from django.contrib.auth.models import AbstractUser 
from django.db import models


class Utilisateur(AbstractUser):
    pass

class Ville(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom")
    code_postal = models.CharField(max_length=5, null=True, blank=True, verbose_name="Code Postal")
    created_at = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='villes')
    #utilisateur.villes.all()

    class Meta:
        unique_together = ('utilisateur','code_postal')

    def __str__(self):
        return f"{self.code_postal} {self.nom}"
 

    
