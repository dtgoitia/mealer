import datetime
from typing import List

import graphene

from src.ingredients.api.graphql import types
from src.ingredients.models import Ingredient


class CreateIngredient(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        unit = graphene.String(required=True)

    ingredient = graphene.Field(types.IngredientGraphqlType)

    @staticmethod
    def mutate(root, info, name: str, unit: str,) -> "CreateIngredient":
        """Create an Ingredient and return it."""
        # TODO: implement service and validations
        # ingredient = IngredientService.create(name=name, unit=unit)
        ingredient = Ingredient(name=name, unit=unit)
        ingredient.save()
        return CreateIngredient(ingredient=ingredient)


class DeleteIngredient(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id: int) -> "DeleteIngredient":
        # TODO: implement service and validations
        ingredient = Ingredient.objects.get(id=id)
        deleted_amount = ingredient.delete()
        if deleted_amount != 1:
            success = False
        success = True
        return DeleteIngredient(success=success)


class Mutation:
    create_ingredient = CreateIngredient.Field()
    delete_ingredient = DeleteIngredient.Field()
