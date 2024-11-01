from django.shortcuts import render
from .models import Category, Recepie
# Create your views here.


def index(request):
    categories = Category.objects.all()
    newest_recepies = Recepie.objects.all().order_by('-updated_at')[:3]
    top_recipes = Recepie.objects.all().order_by('-rating')[:3]
    return render(request, 'recipes/index.html', {
        'categories': categories,
        'newest_recepies': newest_recepies,
        'top_recipes': top_recipes
    })


def recepie_detail(request, slug):
    recipe = Recepie.objects.get(slug=slug)
    return render(request, 'recipes/recipe-detail.html', {
        "recipe": recipe
    })
