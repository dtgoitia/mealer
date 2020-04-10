import datetime
import time
import uuid

from django.core.management.base import BaseCommand

from src.ingredients.models import Ingredient
from src.recipes.models import Recipe, RecipeIngredient


class Command(BaseCommand):
    help = "Creates 2 recipes with ingredients."

    def handle(self, *args, **kwargs):
        # Ingredients
        ingredient_a = Ingredient(name=f"ingredient A", unit="unit")
        ingredient_a.save()
        ingredient_b = Ingredient(name=f"ingredient B", unit="kg")
        ingredient_b.save()

        # Recipe A
        recipe_a = Recipe(name="recipe A")
        recipe_a.save()

        recipe_a_ingredient_a = RecipeIngredient(
            recipe=recipe_a, ingredient=ingredient_a, amount=2
        )
        recipe_a_ingredient_a.save()
        recipe_a_ingredient_b = RecipeIngredient(
            recipe=recipe_a, ingredient=ingredient_b, amount=3
        )
        recipe_a_ingredient_b.save()

        # Recipe B
        recipe_b = Recipe(name="recipe B")
        recipe_b.save()

        recipe_b_ingredient_a = RecipeIngredient(
            recipe=recipe_b, ingredient=ingredient_a, amount=4
        )
        recipe_b_ingredient_a.save()
        recipe_b_ingredient_b = RecipeIngredient(
            recipe=recipe_b, ingredient=ingredient_b, amount=1
        )
        recipe_b_ingredient_b.save()
