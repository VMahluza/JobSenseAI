
import graphene
"""
This module defines the GraphQL schema for user authentication using Django and Graphene.
Classes:
    UserType:
        A DjangoObjectType that represents the User model with selected fields: id, username, email, and role.
    ObtainToken:
        A custom mutation extending graphql_jwt.ObtainJSONWebToken to include the authenticated user in the response.
    Query:
        Defines the root query type for the schema.
        Fields:
            - me: Returns the currently authenticated user. Raises an exception if the user is not authenticated.
    Mutation:
        Defines the root mutation type for the schema.
        Fields:
            - token_auth: Authenticates a user and returns a JSON Web Token.
            - verify_token: Verifies the validity of a JSON Web Token.
            - refresh_token: Refreshes an existing JSON Web Token.
Schema:
    schema:
        The GraphQL schema combining the Query and Mutation types.
"""
from graphene_django.types import DjangoObjectType
import graphql_jwt
from django.contrib.auth import get_user_model

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email", "role")



class ObtainToken(graphql_jwt.ObtainJSONWebToken):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication required!")
        return user

class Mutation(graphene.ObjectType):
    token_auth = ObtainToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
