from django.shortcuts import render
from . models import Article

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
    return render(request, "produits/panier.html")