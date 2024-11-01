from django.contrib import admin
from .models import Recepie, Category

# Register your models here.


# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class RecepieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rating', )
    list_filter = ('category', 'rating', )
    prepopulated_fields = {"slug": ("name", )}


# admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recepie, RecepieAdmin)
