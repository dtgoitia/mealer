from django.db import models

from src.ingredients.models import Ingredient


class Recipe(models.Model):
    name = models.TextField(
        null=False, help_text="Short name for the user to identify the Recipe.",
    )


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, related_name="ingredients", on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        Ingredient, related_name="+", on_delete=models.CASCADE
    )
    amount = models.IntegerField(
        null=False,
        # validators=[MinValueValidator(0)],
        help_text="Amount of units of the given ingredient in the recipe.",
    )
