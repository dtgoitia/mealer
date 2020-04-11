import os
import zipfile

from django.core.management.base import BaseCommand

from ...utils import timestamp
from src.recipes.services import RecipeExporter
from src.ingredients.services import IngredientExporter


def create_backup_file_path(*, target_dir: str) -> str:
    return f"{target_dir}/mealer-backup-{timestamp()}.zip"


class Command(BaseCommand):
    help = "Backup all recipes and their ingredients to a zip file."

    def handle(self, *args, **kwargs):
        current_dir = os.getcwd()
        zip_path = create_backup_file_path(target_dir=current_dir)

        # Generate backup files
        backups_files = []
        ingredients_backup_path = IngredientExporter.export_all(target_dir=current_dir)
        backups_files.append(ingredients_backup_path)
        recipes_backup_path = RecipeExporter.export_all(target_dir=current_dir)
        backups_files.append(recipes_backup_path)

        with zipfile.ZipFile(zip_path, "w") as myzip:
            for path in backups_files:
                file_name = os.path.basename(path)
                myzip.write(path, arcname=file_name)

        # Clean-up if zip successfully created
        for path in backups_files:
            os.remove(path)

        print(f"Backup generated at {zip_path}")
