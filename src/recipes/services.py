import datetime
import os
from typing import Any, Dict, List

import yaml

from .models import Recipe


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
