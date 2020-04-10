# Generated by Django 3.0.5 on 2020-04-10 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ingredients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.TextField(
                        help_text="Short name for the user to identify the Recipe."
                    ),
                ),
                (
                    "preparation",
                    models.TextField(
                        default="", help_text="Steps to prepare the Recipe.", null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RecipeIngredient",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.IntegerField(
                        help_text="Amount of units of the given ingredient in the recipe."
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="ingredients.Ingredient",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ingredients",
                        to="recipes.Recipe",
                    ),
                ),
            ],
        ),
    ]
