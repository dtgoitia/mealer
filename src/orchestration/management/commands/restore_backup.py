import argparse
import os
import shutil
import zipfile

from django.core.management.base import BaseCommand
from django.db import transaction

from ...utils import hash, timestamp

from src.recipes.services import RecipeImporter, RecipeService
from src.ingredients.services import IngredientImporter, IngredientService


PATH_ARGUMENT = "path"
INGREDIENTS_FILE = "ingredients.yml"
RECIPES_FILE = "recipes.yml"


def unzip_backup_file(path: str) -> str:
    """Unzip backup file and return the path of the container directory."""
    with zipfile.ZipFile(path, "r") as zip_ref:
        temp_dir = os.path.join(os.getcwd(), hash())
        zip_ref.extractall(temp_dir)
    return temp_dir


class Command(BaseCommand):
    help = "Backup all recipes and their ingredients to a zip file."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            PATH_ARGUMENT,
            help="absolute path to the backup file to import",
            type=argparse.FileType("r"),
        )

    @transaction.atomic
    def handle(self, *args, **options):
        current_dir = os.getcwd()
        zip_path = options[PATH_ARGUMENT].name

        temp_dir = unzip_backup_file(zip_path)
        ingredients_path = os.path.join(temp_dir, INGREDIENTS_FILE)
        recipes_path = os.path.join(temp_dir, RECIPES_FILE)

        # Clean tables
        IngredientService.delete_all()
        RecipeService.delete_all()

        # Import
        IngredientImporter.import_backup(ingredients_path)
        RecipeImporter.import_backup(recipes_path)

        shutil.rmtree(temp_dir)
