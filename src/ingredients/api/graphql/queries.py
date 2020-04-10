import graphene

from . import types
from ...models import Ingredient


class Query(object):
    ingredients = graphene.List(types.IngredientGraphqlType)

    def resolve_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()
