from django.db import models

from src.ingredients.models import Ingredient


UNITLESS = "-"


class Recipe(models.Model):
    name = models.TextField(
        null=False, help_text="Short name for the user to identify the Recipe.",
    )
    preparation = models.TextField(
        null=True, help_text="Steps to prepare the Recipe.", default=""
    )
    portions = models.IntegerField(
        null=True,
        blank=True,
        # If not specified (blank), means I'm still unsure
        help_text="Number of portions obtained from the Recipe.",
    )
    duration = models.IntegerField(
        null=True,
        blank=True,
        # If not specified (blank), means I'm still unsure
        help_text="Number of minutes it takes to prepare the Recipe.",
    )

    @property
    def markdown(self) -> str:
        ingredients = [self._format_item(item) for item in self.ingredients.all()]
        ingredients_section = "\n".join(ingredients)
        return f"""
# {self.name}

## Ingredients

{ingredients_section if len(ingredients) > 0 else '(no ingredients)'}

## Preparation

{self.preparation if self.preparation else 'no preparation'}
""".strip()

    def _format_item(self, item: "RecipeIngredient") -> str:
        indentation = "  - "
        if item.ingredient.unit == UNITLESS:
            return f"{indentation}{item.ingredient.name}"
        return (
            f"{indentation}{item.amount} {item.ingredient.unit}, {item.ingredient.name}"
        )

    def __str__(self) -> str:
        return self.name


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

    def __str__(self) -> str:
        return f"{self.ingredient.name}, {self.amount} {self.ingredient.unit}"
