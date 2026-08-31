from django.contrib import admin
from .models import Recipe, Category
import logging

# Register your models here.
# Create a logger
logger = logging.getLogger('admin_actions')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def save_model(self, request, obj, form, change):
        if change:  # If the object is being updated
            # check if name is being updated
            old_name = form.instance.__class__.objects.filter(
                id=obj.id).first().name if obj.id else None
            new_name = obj.name

            if old_name != new_name:  # Log only if the 'name' field changed
                logger.info(
                    f"Admin: '{request.user}' Category: '{obj.name}' (ID: '{obj.id}'), Action: 'name update', old name: '{old_name}', new name: '{new_name}'")
            else:
                logger.info(
                    f"Admin {request.user} updated category: {obj.name} (ID: {obj.id})")
        else:  # If the object is being created
            logger.info(
                f"Admin: '{request.user}' Action: Added a new Category: '{obj.name}' (ID: '{obj.id}')")
        super().save_model(request, obj, form, change)

    # Override delete_model to log on delete
    def delete_model(self, request, obj):
        logger.info(
            f"Admin: '{request.user}' Category name: '{obj.name}' (ID: '{obj.id}'), Action: 'category delete'")
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        # If bulk delete is performed, log it for each object
        for obj in queryset:
            logger.info(
                f"Admin: '{request.user}' Category name: '{obj.name}' (ID: '{obj.id}'), Action: 'category delete'")
        super().delete_queryset(request, queryset)


class RecepieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'rating', )
    list_filter = ('category', 'rating', )
    prepopulated_fields = {"slug": ("name", )}

    def save_model(self, request, obj, form, change):
        if change:  # If the object is being updated
            # check if name is being updated
            old_name = form.instance.__class__.objects.filter(
                id=obj.id).first().name if obj.id else None
            new_name = obj.name

            if old_name != new_name:  # Log only if the 'name' field changed
                logger.info(
                    f"Admin: '{request.user}' Recipe: '{obj.name}' (ID: '{obj.id}'), Action: 'name update', old name: '{old_name}', new name: '{new_name}'")

            # check if category is being updated
            old_category = form.instance.__class__.objects.filter(
                id=obj.id).first().category if obj.id else None
            new_category = obj.category

            if old_category != new_category:  # Log only if the 'category' field changed
                logger.info(
                    f"Admin: '{request.user}' Recipe: '{obj.name}' (ID: '{obj.id}'), Action: 'category update', old category: '{old_category}', new category: '{new_category}'")

            # check if ingredients is being updated
            old_ingredients = form.instance.__class__.objects.filter(
                id=obj.id).first().ingredients if obj.id else None
            new_ingredients = obj.ingredients

            if old_ingredients != new_ingredients:  # Log only if the 'ingredients' field changed
                logger.info(
                    f"Admin: '{request.user}' Recipe: '{obj.name}' (ID: '{obj.id}'), Action: 'ingredients update'")

            # check if preparation is being updated
            old_preparation = form.instance.__class__.objects.filter(
                id=obj.id).first().preparation if obj.id else None
            new_preparation = obj.preparation

            if old_preparation != new_preparation:  # Log only if the 'preparation' field changed
                logger.info(
                    f"Admin: '{request.user}' Recipe: '{obj.name}' (ID: '{obj.id}'), Action: 'preparation update'")

            # check if rating is being updated
            old_rating = form.instance.__class__.objects.filter(
                id=obj.id).first().rating if obj.id else None
            new_rating = obj.rating

            if old_rating != new_rating:  # Log only if the 'rating' field changed
                logger.info(
                    f"Admin: '{request.user}' Recipe: '{obj.name}' (ID: '{obj.id}'), Action: 'rating update', old rating: '{old_rating}', new rating: '{new_rating}'")

            # check if image is being updated
            old_image = form.instance.__class__.objects.filter(
                id=obj.id).first().image if obj.id else None
            new_image = obj.image

            if old_image != new_image:  # Log only if the 'image' field changed
                logger.info(
                    f"Admin: '{request.user}' Recipe: '{obj.name}' (ID: '{obj.id}'), Action: 'image update', old image: '{old_image}', new image: '{new_image}'")

            # else:
            #     logger.info(
            #         f"Admin {request.user} updated Recipe: {obj.name} (ID: {obj.id})")
        else:  # If the object is being created
            logger.info(
                f"Admin: '{request.user}' Action: Added a new Recipe: '{obj.name}' (ID: '{obj.id}')")
        super().save_model(request, obj, form, change)

    # Override delete_model to log on delete
    def delete_model(self, request, obj):
        logger.info(
            f"Admin: '{request.user}' Recipe name: '{obj.name}' (ID: '{obj.id}'), Action: 'recipe delete'")
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        # If bulk delete is performed, log it for each object
        for obj in queryset:
            logger.info(
                f"Admin: '{request.user}' Recipe name: '{obj.name}' (ID: '{obj.id}'), Action: 'recipe delete'")
        super().delete_queryset(request, queryset)


# admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecepieAdmin)
