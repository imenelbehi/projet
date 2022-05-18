from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    nom_complet=models.CharField(max_length=200,null=True)
    num_telephone=models.CharField(max_length=200,null=True)
    e_mail=models.EmailField(max_length=200,null=True)
def __str__(self):
    return self.nom_complet