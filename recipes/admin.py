from django.contrib import admin
from .models import Recipe, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class RecepieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rating', )
    list_filter = ('category', 'rating', )
    prepopulated_fields = {"slug": ("name", )}


# admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecepieAdmin)
