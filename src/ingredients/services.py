import datetime
import os
from typing import Any, Dict, List

import yaml

from .models import Ingredient


class IngredientExporter:
    @classmethod
    def export_all(cls, *, target_dir: str) -> str:
        """Create a backup file.
        
        If successful, returns created file path.
        """
        path = cls.create_backup_file_path(target_dir)
        with open(path, "w") as f:
            data = {"ingredients": cls._generate_data()}
            yaml.safe_dump(data, f, sort_keys=False)
        return path

    def create_backup_file_path(target_dir: str) -> str:
        return f"{target_dir}/ingredients.yml"

    @classmethod
    def _generate_data(cls) -> List[Dict[str, Any]]:
        return [
            cls._generate_ingredient_data(ingredient)
            for ingredient in Ingredient.objects.all()
        ]

    @staticmethod
    def _generate_ingredient_data(ingredient: Ingredient) -> Dict[str, Any]:
        return {
            "id": ingredient.id,
            "name": ingredient.name,
            "unit": ingredient.unit,
        }
