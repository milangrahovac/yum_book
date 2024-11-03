from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
import os
from django.conf import settings


class Category(models.Model):
    name = models.CharField(unique=True, max_length=30)

    class Meta():
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def recepie_category(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower().title()
        super().save(*args, **kwargs)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    ingredients = models.TextField(max_length=300)
    preparation = models.TextField(
        validators=[MinLengthValidator(10), MaxLengthValidator(2000)])
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.ImageField(upload_to='images')
    date = models.DateField(auto_now=True)
    # captures creation time
    created_at = models.DateTimeField(auto_now_add=True)
    # updates to current time on save
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower().title()
        # Check if this is an update and if the image is being changed
        if self.pk:
            try:
                old_image = Recipe.objects.get(pk=self.pk).image
                # If a new image is set and the old image path exists, delete the old image
                if old_image and old_image != self.image:
                    old_image_path = os.path.join(
                        settings.MEDIA_ROOT, old_image.name)
                    if os.path.isfile(old_image_path):
                        os.remove(old_image_path)
            except Recipe.DoesNotExist:
                pass  # If the object doesn't exist, this is a new instance, so skip this

        # Call the superclass save method to save the new image and any other changes
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image file from the filesystem
        if self.image:
            try:
                # Construct the full file path
                file_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
                if os.path.isfile(file_path):
                    os.remove(file_path)  # Remove the file
            except Exception as e:
                # Handle any exceptions that might occur during file deletion
                print(f"Error deleting file {file_path}: {e}")

        # Call the superclass's delete method to remove the instance from the database
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Recepies'
