from django.contrib import admin

from . models import Categorie, Images, Produit, Article


class CategorieAdmin(admin.ModelAdmin):
 list_display = ("nom", "description")

class ImagesInline(admin.TabularInline):
    model = Comment
    extra = 1 # Show one empty comment form by default



class ProduitAdmin(admin.ModelAdmin):
    list_display = ("nom", "description", "categorie")
    inlines = [CommentInline]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("nom", "prix", "date_added", "marque", "couleur",)
    inlines = [CommentInline]
