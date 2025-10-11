from django.db import models

# Create your models here.
"""
Categorie:
    nom, description

produit:
    nom, description, images, date_added, Categorie

Article:
   nom, decoration, prix, images, date_added, marque, couleur,

"""
class Categorie(models.Model):
    nom = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = true)

    def __str__(self):
        return f"{self.nom}"
