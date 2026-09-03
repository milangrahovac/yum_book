import csv
from collections import Counter
from pathlib import Path

from django.conf import settings
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    recipe = get_object_or_404(Recipe, slug=slug)
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


def admin_dashboard(request):
    log_lines = _read_admin_log_lines()
    category_stats = list(
        Category.objects.annotate(recipe_count=Count('recipe')).values(
            'name', 'recipe_count'
        ).order_by('-recipe_count', 'name')
    )
    max_category_count = max(
        (item['recipe_count'] for item in category_stats), default=1
    )
    activity_by_day = Counter(line[:10]
                              for line in log_lines if len(line) >= 10)

    return render(request, 'recipes/admin-dashboard.html', {
        'recipe_count': Recipe.objects.count(),
        'category_count': Category.objects.count(),
        'average_rating': Recipe.objects.aggregate(avg=Avg('rating'))['avg'],
        'category_stats': category_stats,
        'max_category_count': max_category_count,
        'activity_by_day': sorted(activity_by_day.items(), reverse=True)[:7],
    })


def admin_actions_log(request):
    log_lines = _read_admin_log_lines()
    return render(request, 'recipes/admin-actions-log.html', {
        'log_text': '\n'.join(reversed(log_lines[-200:])),
    })


def export_admin_actions_log(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="admin_actions.csv"'
    writer = csv.writer(response)
    writer.writerow(['log_entry'])
    writer.writerows([[line] for line in _read_admin_log_lines()])
    return response


def _read_admin_log_lines():
    log_path = Path(settings.LOG_DIR) / 'admin_actions.log'
    if not log_path.exists():
        return []
    return log_path.read_text(encoding='utf-8').splitlines()


def get_chart_version(chart_path="helm/Chart.yaml"):
    with open(chart_path, 'r') as stream:
        try:
            chart = yaml.safe_load(stream)
            return chart.get("appVersion", None)
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")
            return None
