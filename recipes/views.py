from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Category, Recepie
# Create your views here.


def index(request):
    # View that renders the home page.
    # always return "categories" so dropdown menu can be created

    categories = Category.objects.all()
    newest_recepies = Recepie.objects.all().order_by('-updated_at')[:3]
    top_recipes = Recepie.objects.all().order_by('-rating')[:3]
    return render(request, 'recipes/index.html', {
        'categories': categories,
        'newest_recepies': newest_recepies,
        'top_recipes': top_recipes
    })


def recepie_detail(request, slug):
    # Single recipe details page
    # always return "categories" so dropdown menu can be created
    categories = Category.objects.all()
    recipe = Recepie.objects.get(slug=slug)
    return render(request, 'recipes/recipe-detail.html', {
        'categories': categories,
        'recipe': recipe
    })


def all_recipes(request):
    # All Recipes page
    # always return "categories" so dropdown menu can be created
    categories = Category.objects.all()
    all_recepies = Recepie.objects.all().order_by('-updated_at')
    return render(request, 'recipes/all-recipes.html', {
        'categories': categories,
        'all_recepies': all_recepies
    })


def recipes_by_category(request, selected_category):
    # When user click on category should be redirected to page to see all recipes with selected category
    # always return "categories" so dropdown menu can be created
    categories = Category.objects.all()

    # Retrieve the Category object based on the name from the URL
    category_obj = get_object_or_404(Category, name=selected_category)

    # Filter Recepie objects where category matches the retrieved category
    recipes = Recepie.objects.filter(category=category_obj)

    return render(request, 'recipes/category.html', {
        'category': selected_category,
        'categories': categories,
        'selected_recipes': recipes,
    })
