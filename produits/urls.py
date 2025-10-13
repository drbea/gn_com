from django.urls import path

from . import views

app_name = "produits"

urlpatterns = [
    path("", views.index, name = "index"),
    path("panier/", views.panier, name = "panier"),
    path("<int:id_produit>/", views.detail_article, name = "detail")
]
