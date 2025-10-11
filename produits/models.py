from django.db import models

# Create your models here.
"""
Categorie:
    nom, description

produit:
    nom, description, images, date_added, Categorie

Article:
   nom, description, prix, images, date_added, marque, couleur,

"""
class Categorie(models.Model):
    nom = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = true)

    def __str__(self):
        return f"{self.nom}"

class Images(models.Model):
    nom = models.CharField(max_length = 100, blank=True)
    def __str__(self):
        return f"{self.nom}"



class Produit(models.Model):
    nom = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = true)
    images = models.ForeignKey(Images, on_delete = models.CASCADE, blank = True)
    date_added = models.DateTimeField(aut_now = True)
    categorie =  models.ForeignKey(Categorie, on_delete = models.CASCADE, blank = True)

    def __str__(self):
        return f"{self.nom}"


class Article(models.Model):
    nom = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = true)
    images = models.ForeignKey(Images, on_delete = models.CASCADE, blank = True)
    date_added = models.DateTimeField(aut_now = True)
    categorie =  models.ForeignKey(Categorie, on_delete = models.CASCADE, blank = True)
    marque =  models.CharField(max_length = 100, blank = True)
    couleur = models.CharField(max_length = 100, blank = True)
    prix = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return f"{self.nom}"
