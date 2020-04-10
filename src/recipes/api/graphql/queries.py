import graphene
from graphene_django.types import DjangoObjectType

from src.recipes.api.graphql import types
from src.recipes.models import Recipe


class Query(object):
    recipes = graphene.List(types.RecipeGraphqlType)

    def resolve_recipes(self, info, **kwargs):
        return Recipe.objects.all()
