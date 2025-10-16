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
    description = models.TextField(blank = True)

    def __str__(self):
        return f"{self.nom}"




class Produit(models.Model):
    nom = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = True)
    date_added = models.DateTimeField(auto_now = True)
    categorie =  models.ForeignKey(Categorie, on_delete = models.CASCADE, blank = True)

    def __str__(self):
        return f"{self.nom}"


class Article(models.Model):
    nom = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = True)
    date_added = models.DateTimeField(auto_now = True)
    produit =  models.ForeignKey(Produit, on_delete = models.CASCADE, blank = True, default="")
    marque =  models.CharField(max_length = 100, blank = True)
    couleur = models.CharField(max_length = 100, blank = True)
    prix = models.DecimalField(max_digits = 15, decimal_places = 2)

    def __str__(self):
        return f"{self.nom}"


class ImagesArticle(models.Model):
    nom = models.CharField(max_length = 100, blank=True)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, blank = True, related_name="images")
    image_file = models.ImageField(upload_to='article_images/', null=True)

    def __str__(self):
        return f"Image pour {self.article}"

class Commande(models.Model):
    date_commande = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    nom_client = models.CharField(max_length = 100, blank = True, null = True)
    def __str__(self):
        return f"Commande {self.id} - {self.date_commande}"

class ArticleCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.article.nom} x {self.quantite}"

#
# class ImagesProduit(models.Model):
#     nom = models.CharField(max_length = 100, blank=True)
#     produit = models.ForeignKey(Produit, on_delete = models.CASCADE, blank = True, related_name="images")
#     image_file = models.ImageField(upload_to='produit_images/', null=True)
#
#     def __str__(self):
#         return f"Image pour {self.produit}"
#






#
