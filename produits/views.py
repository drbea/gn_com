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
