from django.contrib import admin

# Register your models here.
import movies
from movies.models import Actor, Movie

admin.site.register(Actor)
admin.site.register(Movie)
