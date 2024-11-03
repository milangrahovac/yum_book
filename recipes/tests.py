# from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe
from django.utils import timezone

# from django.core.exceptions import ValidationError


test1 = {
    'name': 'Spaghetti Carbonara',
    'slug': 'spaghetti-carbonara',
    'ingredients': 'Spaghetti, eggs, pancetta, cheese',
    'preparation': 'Boil spaghetti. Cook pancetta. Mix with eggs and cheese.',
    'rating': 4,
    'image=': 'images/spaghetti3234.jpg',
    'category': 'Italian',
}

test2 = {
    'name': 'Sushi Maki',
    'slug': 'sushi-maki',
    'ingredients': 'Rice, fish',
    'preparation': 'Prepare rice. Slice fish. Roll with seaweed.',
    'rating': 5,
    'image=': 'images/sushi4343.jpg',
    'category': 'Asian',
}


class HomepageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = Category.objects.create(name=test1['category'])
        cls.category2 = Category.objects.create(name=test2['category'])

        cls.recipe1 = Recipe.objects.create(
            name=test1['name'],
            slug=test1['slug'],
            ingredients=test1['ingredients'],
            preparation=test1['preparation'],
            rating=test1['rating'],
            image=test1['image='],
            category=cls.category1,
        )

        cls.recipe2 = Recipe.objects.create(
            name=test2['name'],
            slug=test2['slug'],
            ingredients=test2['ingredients'],
            preparation=test2['preparation'],
            rating=test2['rating'],
            image=test2['image='],
            category=cls.category2,
        )

    def test_index_view(self):
        # Test the home page view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('categories', response.context)
        self.assertIn('newest_recipes', response.context)
        self.assertIn('top_recipes', response.context)
        # Checks for the 3 latest recipes
        self.assertLessEqual(len(response.context['newest_recipes']), 3)
        # Checks for the top 3 rated recipes
        self.assertLessEqual(len(response.context['top_recipes']), 3)

    def test_all_recipes_view(self):
        # Test the requiest status and context
        response = self.client.get(reverse('all_recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/all-recipes.html')
        self.assertIn('categories', response.context)
        self.assertIn('all_recipes', response.context)

    def test_recipe_detail_view(self):
        # Test the recipe detail page view
        response = self.client.get(
            reverse('recipe-detail-page', args=[self.recipe1.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe-detail.html')
        self.assertIn('categories', response.context)
        self.assertEqual(
            response.context['recipe'].name, test1['name'])

    def test_recipes_by_category_view(self):
        # Test the recipes by category
        response = self.client.get(
            reverse('recipes_by_category', args=[self.category2.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/category.html')
        self.assertEqual(
            response.context['category'], test2['category'])
        self.assertIn('category', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('selected_recipes', response.context)

    def test_recipes_rating(self):
        # Check that all recipes in 'all_recipes' have a rating >= 1 and <= 5
        response = self.client.get(reverse('all_recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/all-recipes.html')
        self.assertIn('all_recipes', response.context)

        recipes = response.context['all_recipes']

        for recipe in recipes:
            self.assertGreaterEqual(recipe.rating, 1)
            self.assertLessEqual(recipe.rating, 5)

    def test_recipes_slug(self):
        # Check that all recipes in 'all_recipes' have a rating >= 1 and <= 5
        response = self.client.get(reverse('all_recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('all_recipes', response.context)

        recipes = response.context['all_recipes']

        for recipe in recipes:
            self.assertGreaterEqual(recipe.rating, 1)
            self.assertLessEqual(recipe.rating, 5)
            self.assertTrue(recipe.slug.islower())
            self.assertNotIn(" ", recipe.slug)

    def test_date_time(self):
        # check if created_at and updated_at are in datetime format
        # check if created_at stay the same after Recipe update
        # check if update_at get a new datetime after update

        response = self.client.get(reverse('all_recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('all_recipes', response.context)
        recipes = response.context['all_recipes']

        for recipe in recipes:
            # Check if created_at and updated_at are in datetime format
            self.assertIsInstance(recipe.created_at, timezone.datetime)
            self.assertIsInstance(recipe.updated_at, timezone.datetime)

            # Store the original updated_at time
            original_name = recipe.name
            original_updated_at = recipe.updated_at
            original_created_at = recipe.created_at

            # Update the recepie and save
            recipe.name = "Updated Chocolate Cake"
            recipe.save()

            # check if name has been changed to a new name
            self.assertNotEqual(recipe.name, original_name)

            # After update update_at time should be auto changed to a new datetime
            # Check if updated_at has been changed to a new datetime
            self.assertNotEqual(recipe.updated_at, original_updated_at)
            self.assertGreater(recipe.updated_at, original_updated_at)

            # Check if crated_at time still has a same datetime
            self.assertEqual(original_created_at, recipe.created_at)

    # class HomepageTest(TestCase):
    #     @classmethod
    #     def setUpTestData(cls):
    #         cls.category1 = Category.objects.create(name="italian")
    #         cls.category2 = Category.objects.create(name="asian")

    #         cls.recipe1 = Recepie.objects.create(
    #             name="Spaghetti Carbonara",
    #             slug="spaghetti-carbonara",
    #             ingredients="Spaghetti, eggs, pancetta, cheese",
    #             preparation="Boil spaghetti. Cook pancetta. Mix with eggs and cheese.",
    #             rating=4,
    #             image="images/spaghetti3234.jpg",
    #             category=cls.category1
    #         )

    #         cls.recipe2 = Recepie.objects.create(
    #             name="Sushi",
    #             slug="sushi",
    #             ingredients="Rice, fish, seaweed",
    #             preparation="Prepare rice. Slice fish. Roll with seaweed.",
    #             rating=5,
    #             image="images/sushi2032.jpg",
    #             category=cls.category2
    #         )

    #     def test_index_view(self):
    #         # Test the home page view
    #         response = self.client.get(reverse('index'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn('categories', response.context)
    #         self.assertIn('newest_recepies', response.context)
    #         self.assertIn('top_recipes', response.context)
    #         # Checks for the 3 latest recipes
    #         self.assertLessEqual(len(response.context['newest_recepies']), 3)
    #         # Checks for the top 3 rated recipes
    #         self.assertLessEqual(len(response.context['top_recipes']), 3)

    #     def test_all_recipes_view(self):
    #         # Test the all recipes page view
    #         response = self.client.get(reverse('all_recipes'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertTemplateUsed(response, 'recipes/all-recipes.html')
    #         self.assertIn('categories', response.context)
    #         self.assertIn('all_recepies', response.context)

    #     def test_recipe_detail_view(self):
    #         # Test the recipe detail page view
    #         response = self.client.get(
    #             reverse('recipe-detail-page', args=[self.recipe1.slug]))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertTemplateUsed(response, 'recipes/recipe-detail.html')
    #         self.assertIn('categories', response.context)
    #         self.assertEqual(
    #             response.context['recipe'].name, "Spaghetti Carbonara")

    #     def test_recipes_by_category_view(self):
    #         # Test the recipes by category view for "Italian"
    #         response = self.client.get(
    #             reverse('recipes_by_category', args=[self.category1.name]))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertTemplateUsed(response, 'recipes/category.html')
    #         self.assertIn('category', response.context)
    #         self.assertIn('categories', response.context)
    #         self.assertIn('selected_recipes', response.context)

    #     def test_recipes_by_category_not_found(self):
    #         # Test the recipes by category view with a non-existent category
    #         response = self.client.get(
    #             reverse('recipes_by_category', args=["NonExistentCategory"]))
    #         self.assertEqual(response.status_code, 404)
