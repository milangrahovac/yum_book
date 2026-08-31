# from django.contrib import admin
# from .models import Recipe, Category
# import logging

# # Register your models here.
# # Create a logger
# logger = logging.getLogger('admin_actions')


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', )


# class RecepieAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'rating', )
#     list_filter = ('category', 'rating', )
#     prepopulated_fields = {"slug": ("name", )}

#     def save_model(self, request, obj, form, change):
#         if change:  # If the object is being updated
#             logger.info(
#                 f"Admin {request.user} updated Recipe: {obj.name} (ID: {obj.id})")
#         else:  # If the object is being created
#             logger.info(
#                 f"Admin {request.user} added a new Recipe: {obj.name} (ID: {obj.id})")
#         super().save_model(request, obj, form, change)

#     # Override delete_model to log on delete
#     def delete_model(self, request, obj):
#         logger.info(
#             f"Admin {request.user} deleted Recipe: {obj.name} (ID: {obj.id})")
#         super().delete_model(request, obj)

#     def delete_queryset(self, request, queryset):
#         # If bulk delete is performed, log it for each object
#         for obj in queryset:
#             logger.info(
#                 f"Admin {request.user} deleted Recipe: {obj.name} (ID: {obj.id})")
#         super().delete_queryset(request, queryset)


# # admin.site.register(Ingredient, IngredientAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Recipe, RecepieAdmin)
