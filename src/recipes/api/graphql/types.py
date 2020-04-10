import graphene
from graphene_django.types import DjangoObjectType

from src.recipes.models import Recipe, RecipeIngredient


class RecipeGraphqlType(DjangoObjectType):
    class Meta:
        model = Recipe
