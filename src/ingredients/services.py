import datetime
import os
from typing import Any, Dict, List, NoReturn, Optional

from django.db import transaction
import yaml

from .models import Ingredient


class IngredientService:
    @staticmethod
    def delete_all() -> Optional[NoReturn]:
        Ingredient.objects.all().delete()


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


class IngredientImporter:
    @staticmethod
    @transaction.atomic
    def import_backup(path: str) -> None:
        """Import new tables.
        
        It assumes the table is clean.
        """
        with open(path, "r") as f:
            data = yaml.full_load(f)

        for item in data["ingredients"]:
            # TODO: optimize with bulk import
            ingredient = Ingredient(id=item["id"], name=item["name"], unit=item["unit"])
            ingredient.save()
