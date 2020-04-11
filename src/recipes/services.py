import datetime
import os
from typing import Any, Dict, List, NoReturn, Optional

import yaml
from django.db import transaction

from .models import Recipe, RecipeIngredient


class RecipeService:
    @staticmethod
    @transaction.atomic
    def import_recipe(
        *,
        id: int,
        name: str,
        preparation: Optional[str] = None,
        portions: Optional[int] = None,
        duration: Optional[int] = None,
        ingredient_entries: List[Dict[str, Any]],
    ) -> None:
        recipe = Recipe(
            id=id,
            name=name,
            preparation=preparation,
            portions=portions,
            duration=duration,
        )
        recipe.save()
        for entry in ingredient_entries:
            # TODO: optimize with bulk
            RecipeIngredient(
                recipe_id=recipe.id,
                # The Ingredient ID must exist by this time
                # Make sure to import the Ingredient backup first
                ingredient_id=entry["id"],
                amount=entry["amount"],
            ).save()

    @staticmethod
    def delete_all() -> Optional[NoReturn]:
        Recipe.objects.all().delete()


class RecipeExporter:
    @classmethod
    def export_all(cls, *, target_dir: str) -> str:
        """Create a backup file.
        
        If successful, returns created file path.
        """
        path = cls.create_backup_file_path(target_dir)
        with open(path, "w") as f:
            data = {"recipes": cls._generate_data()}
            yaml.safe_dump(data, f, sort_keys=False)
        return path

    def create_backup_file_path(target_dir: str) -> str:
        return f"{target_dir}/recipes.yml"

    @classmethod
    def _generate_data(cls) -> List[Dict[str, Any]]:
        return [cls._generate_recipe_data(recipe) for recipe in Recipe.objects.all()]

    @staticmethod
    def _generate_recipe_data(recipe: Recipe) -> Dict[str, Any]:
        recipe_ingredients = [
            {"id": entry.ingredient_id, "amount": entry.amount}
            for entry in recipe.ingredients.all()
        ]
        return {
            "id": recipe.id,
            "name": recipe.name,
            "preparation": recipe.preparation,
            "ingredients": recipe_ingredients,
            "portions": recipe.portions,
            "duration": recipe.duration,
        }


class RecipeImporter:
    @staticmethod
    @transaction.atomic
    def import_backup(path: str) -> None:
        """Import new recipese.
        
        It assumes the table is clean.
        """
        with open(path, "r") as f:
            data = yaml.full_load(f)

        for recipe in data["recipes"]:
            # TODO: optimize with bulk import
            RecipeService.import_recipe(
                id=recipe["id"],
                name=recipe["name"],
                preparation=recipe["preparation"],
                portions=recipe["portions"],
                duration=recipe["duration"],
                ingredient_entries=recipe["ingredients"],
            )
