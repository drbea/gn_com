from django.contrib import admin

from . models import Categorie, Produit, Article, ImagesArticle# ImagesProduit, ,


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
 list_display = ("nom", "description")


# class ImagesProduitInline(admin.TabularInline):
#     model = ImagesProduit
#     fk_name = 'produit' # Spécifie la clé étrangère dans le modèle Images
#     extra = 1

class ImagesArticleInline(admin.TabularInline):
    model = ImagesArticle
    fk_name = 'article' # Spécifie la clé étrangère dans le modèle Images
    extra = 1


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("nom", "description", "categorie")
    # inlines = [ImagesProduitInline]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("nom", "prix", "date_added", "marque", "couleur",)
    inlines = [ImagesArticleInline]
