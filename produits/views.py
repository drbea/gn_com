from django.shortcuts import render


def index(request):

    context = {
        
    }
    return render(request, "produits/index.html", context)
