# from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .models import Category, Recepie
# from django.core.exceptions import ValidationError


test1 = {
    'name': 'Spaghetti Carbonara',
    'slug': 'spaghetti-carbonara',
    'ingredients': 'Spaghetti, eggs, pancetta, cheese',
    'preparation': 'Boil spaghetti. Cook pancetta. Mix with eggs and cheese.',
    'rating': 4,
    'image=': 'images/spaghetti3234.jpg',
    'category': 'italian',
}

test2 = {
    'name': 'Sushi Maki',
    'slug': 'sushi-maki',
    'ingredients': 'Rice, fish',
    'preparation': 'Prepare rice. Slice fish. Roll with seaweed.',
    'rating': 5,
    'image=': 'images/sushi4343.jpg',
    'category': 'asian',
}


class HomepageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category1 = Category.objects.create(name=test1['category'])
        cls.category2 = Category.objects.create(name=test2['category'])

        cls.recipe1 = Recepie.objects.create(
            name=test1['name'],
            slug=test1['slug'],
            ingredients=test1['ingredients'],
            preparation=test1['preparation'],
            rating=test1['rating'],
            image=test1['image='],
            category=cls.category1,
        )

        cls.recipe2 = Recepie.objects.create(
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
        self.assertIn('newest_recepies', response.context)
        self.assertIn('top_recipes', response.context)
        # Checks for the 3 latest recipes
        self.assertLessEqual(len(response.context['newest_recepies']), 3)
        # Checks for the top 3 rated recipes
        self.assertLessEqual(len(response.context['top_recipes']), 3)

    def test_all_recipes_view(self):
        # Test the all recipes page view
        response = self.client.get(reverse('all_recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/all-recipes.html')
        self.assertIn('categories', response.context)
        self.assertIn('all_recepies', response.context)

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
        # Test the recipes by category view for "Italian"
        response = self.client.get(
            reverse('recipes_by_category', args=[self.category2.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/category.html')
        self.assertEqual(
            response.context['category'], test2['category'])
        self.assertIn('category', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('selected_recipes', response.context)

    # def test_recipes_by_category_not_found(self):
    #     # Test the recipes by category view with a non-existent category
    #     response = self.client.get(
    #         reverse('recipes_by_category', args=["NonExistentCategory"]))
    #     self.assertEqual(response.status_code, 404)

        # lol

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
