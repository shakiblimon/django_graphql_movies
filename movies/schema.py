__version__ ="1.0.1"
__author__ = "Shakib Limon"

import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from movies.models import Actor, Movie, Hero


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie


'''
        New Segment with graphql hero and movie 
'''

class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


####    new segment added end     ####


class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    movie = graphene.Field(MovieType, id=graphene.Int())
    actors = graphene.List(ActorType)
    movies = graphene.List(MovieType)
    heros = graphene.List(HeroType)         # Newly Added segment for new model hero

    def resolve_heroes(self, info, **kwargs):
        return Hero.objects.all()
    #################   New Segment Added Finished  ##########################

    def resolve_actor(self,info, **kwargs):
        """
        :param info:
        :param kwargs:
        :return:
        """
        id = kwargs.get('id')

        if id is not None:
            return Actor.objects.get(pk=id)
        return None

    def resolve_movie(self,info,**kwargs):
        """
        :param info:
        :param kwargs:
        :return:
        """
        id = kwargs.get('id')

        if id is not None:
            return Movie.objects.get(pk=id)
        return None


    def resolve_actors(self,info,**kwargs):
        """
        :param info:
        :param kwargs:
        :return:
        """
        return Actor.objects.all()

    def resolve_movies(self,info,**kwargs):
        """
        :param info:
        :param kwargs:
        :return:
        """
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
        """
        :param root:
        :param info:
        :param input:
        :return:
        """
        ok = True
        actor_instance = Actor(name=input.name)
        actor_instance.save()
'''
    Update Actor mutation
'''
class UpdateActor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required =True)
        input = ActorInput(required = True)

    ok = graphene.Boolean()
    actor = graphene.Field(ActorType)

    @staticmethod

    def mutate(root, info , input = None):
        """
        :param root:
        :param info:
        :param input:
        :return:
        """
        ok = False
        actor_instance = Actor.objects.get(pk=id)

        if actor_instance:
            ok = True
            actor_instance.name = input.name
            actor_instance.save()
            return UpdateActor(ok=ok,actor=actor_instance)
        return UpdateActor(ok=ok,actor =None)


'''
       Create mutations for movie
'''

class CreateMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required = True)

    ok = graphene.Boolean()
    actor = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, input = None):
        """
        :param root:
        :param info:
        :param input:
        :return:
        """
        ok = True
        actors = []
        for actor_input in input.actors:
            actor = Actor.objects.get(pk=actor_input.id)
            if actor is None:
                return CreateMovie(ok=False, movie=None)
            actors.append(actor)
        movie_instance = Movie(
            title=input.title,
            year=input.year
        )
        movie_instance.save()
        movie_instance.actors.set(actors)
        return CreateMovie(ok=ok, movie=movie_instance)


'''
       Create mutation for update movie
'''
class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = MovieInput(required = True)

    ok = graphene.Boolean()
    movie = graphene.Field(MovieType)

    @staticmethod

    def mutate(root,info,id, input=None):
        """
        :param root:
        :param info:
        :param id:
        :param input:
        :return:
        """
        ok = False
        movie_instance = Movie.objects.get(pk=id)
        if movie_instance:
            ok = True
            actors = []
            for actor_input in input.actors:
                actor = Actor.objects.get(pk=actor_input.id)
                if actor is None:
                    return CreateMovie(ok=False, movie=None)
                actors.append(actor)
            movie_instance = Movie(
                title=input.title,
                year=input.year
            )
            movie_instance.save()
            movie_instance.actors.set(actors)
            return UpdateMovie(ok=ok, movie=movie_instance)
        return UpdateMovie(ok=ok, movie=None)

# All object mutation

class Mutation(graphene.ObjectType):
    create_actor = CreateActor.Field()
    update_actor = UpdateActor.Field()
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()










