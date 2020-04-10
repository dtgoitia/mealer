import graphene
from graphene_django.types import DjangoObjectType

from src.ingredients.models import Ingredient


class IngredientGraphqlType(DjangoObjectType):
    class Meta:
        model = Ingredient
