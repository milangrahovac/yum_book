from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta():
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def recepie_category(self):
        return self.name


class Recepie(models.Model):
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

    class Meta:
        verbose_name_plural = 'Recepies'

    def __str__(self):
        return self.name
