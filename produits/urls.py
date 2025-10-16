from django.urls import path

from . import views

app_name = "produits"

urlpatterns = [
    path("", views.index, name = "index"),
    path("panier/", views.panier, name = "panier"),
     path("enregistrer-panier/", views.enregistrer_panier, name="enregistrer_panier"),
    path("<int:id_produit>/", views.detail_article, name = "detail"),
]
