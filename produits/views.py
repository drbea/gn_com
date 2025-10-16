from django.shortcuts import render
from . models import Article, Commande, ArticleCommande


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    # articles = Article.objects.select_related("produit").order_by("-date_added")
    articles = Article.objects.prefetch_related('images').all()
    articles_recent = articles[:3]
    print(articles)
    context = {
        "articles": articles,
        "articles_recent": articles_recent
    }
    return render(request, "produits/index.html", context)


def detail_article(request, id_produit):
    article =  Article.objects.get(id = id_produit)
    context = {
        "article": article
    }
    return render(request, "produits/detail_article.html", context)

def panier(request):

    # if request.method == "POST":
        # try:
        #     data = json.loads(request.body)
        #     panier = data.get("panier", [])
        #     total = data.get("total", 0)

        #     # Créer une nouvelle commande
        #     commande = Commande.objects.create(total=total)

        #     # Ajouter les articles à la commande
        #     for article_data in panier:
        #         article = Article.objects.get(nom=article_data["nom"])
        #         ArticleCommande.objects.create(
        #             commande=commande,
        #             article=article,
        #             quantite=article_data["quantite"],
        #             prix_unitaire=article_data["prix"]
        #         )

        #     return JsonResponse({"success": True, "commande_id": commande.id})
        # except Exception as e:
        #     return JsonResponse({"success": False, "error": str(e)}, status=400)
    return render(request, "produits/panier.html")





@csrf_exempt
def enregistrer_panier(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            panier = data.get("panier", [])
            total = data.get("total", 0)
            nom_client = data.get("nom_client")

            # Créer une nouvelle commande
            commande = Commande.objects.create(total=total, nom_client = nom_client)

            # Ajouter les articles à la commande
            for article_data in panier:
                article = Article.objects.get(nom=article_data["nom"])
                ArticleCommande.objects.create(
                    commande=commande,
                    article=article,
                    quantite=article_data["quantite"],
                    prix_unitaire=article_data["prix"]
                )

            return JsonResponse({"success": True, "commande_id": commande.id})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
    return JsonResponse({"success": False, "error": "Méthode non autorisée"}, status=405)
