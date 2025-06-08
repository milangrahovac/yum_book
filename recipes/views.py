from django.shortcuts import render, get_object_or_404
from django.db import connections
from django.db.utils import OperationalError
from django.http import JsonResponse
from .models import Category, Recipe
import yaml
# Create your views here.


def index(request):
    # View that renders the home page.
    # always return "categories" so dropdown menu can be created
    version = get_chart_version()
    categories = Category.objects.all()
    newest_recipes = Recipe.objects.all().order_by('-updated_at')[:3]
    top_recipes = Recipe.objects.all().order_by('-rating')[:3]
    return render(request, 'recipes/index.html', {
        "app_version": version,
        'categories': categories,
        'newest_recipes': newest_recipes,
        'top_recipes': top_recipes
    })


def recepie_detail(request, slug):
    # Single recipe details page
    # always return "categories" so dropdown menu can be created
    categories = Category.objects.all()
    recipe = Recipe.objects.get(slug=slug)
    return render(request, 'recipes/recipe-detail.html', {
        'categories': categories,
        'recipe': recipe
    })


def all_recipes(request):
    # All Recipes page
    # always return "categories" so dropdown menu can be created
    categories = Category.objects.all()
    all_recipes = Recipe.objects.all().order_by('-rating')
    return render(request, 'recipes/all-recipes.html', {
        'categories': categories,
        'all_recipes': all_recipes
    })


def recipes_by_category(request, selected_category):
    # When user click on category should be redirected to page to see all recipes with selected category
    # always return "categories" so dropdown menu can be created
    categories = Category.objects.all()

    # Retrieve the Category object based on the name from the URL
    category_obj = get_object_or_404(Category, name=selected_category)

    # Filter Recepie objects where category matches the retrieved category
    recipes = Recipe.objects.filter(category=category_obj)

    return render(request, 'recipes/category.html', {
        'category': selected_category,
        'categories': categories,
        'selected_recipes': recipes,
    })


def get_chart_version(chart_path="helm/Chart.yaml"):
    with open(chart_path, 'r') as stream:
        try:
            chart = yaml.safe_load(stream)
            return chart.get("appVersion", None)
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")
            return None
