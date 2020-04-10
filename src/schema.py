import graphene

import src.ingredients.api.graphql.queries
import src.ingredients.api.graphql.mutations
import src.recipes.api.graphql.queries


class Query(
    src.ingredients.api.graphql.queries.Query,
    graphene.ObjectType,
):
    pass


class Mutation(src.ingredients.api.graphql.mutations.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
