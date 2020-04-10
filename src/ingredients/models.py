from django.db import models


class Ingredient(models.Model):
    name = models.TextField(
        null=False, help_text="Short name for the user to identify the ingredient.",
    )
    # Until you decide how to model the units, just make them a string
    unit = models.TextField(
        null=False, help_text="Unit of measure for the ingredient.",
    )
