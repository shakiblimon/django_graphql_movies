import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from movies.models import Actor, Movie


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    movie = graphene.Field(MovieType, id=graphene.Int())
    actors = graphene.List(ActorType)
    movies = graphene.List(MovieType)

    def resolve_actor(self,info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Actor.objects.get(pk=id)
        return None

    def resolve_movie(self,info,**kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Movie.objects.get(pk=id)
        return None


    def resolve_actors(self,info,**kwargs):
        return Actor.objects.all()

    def resolve_movies(self,info,**kwargs):
        return Movie.objects.all()


#Making Mutation

class ActorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class MovieInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    actors = graphene.List(ActorInput)
    year = graphene.Int()



'''
    create mutation for actors
'''
class CreateActor(graphene.Mutation):
    class Arguments:
        input = ActorInput(required = True)

    ok = graphene.Boolean()
    actor = graphene.Field(ActorType)

    @staticmethod

    def mutate(root, info, input = None):
        ok = True
        actor_instance = Actor(name=input.name)
        actor_instance.save()






