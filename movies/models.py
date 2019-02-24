__version__ ="1.0.1"
__author__ = "Shakib Limon"

from django.db import models

# Create your models here.

class Actor(models.Model):
     name = models.CharField(max_length=100)

     def __str__(self):
         """
         :return:
         """
         return self.name

     class Meta:
         ordering = ('name',)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    year = models.IntegerField()

    def __str__(self):
        """
        :return:
        """
        return self.title

    class Meta:
        ordering = ('title',)


'''
            Add another model 
'''

class Hero(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=(('M','Male'),('F','Female')), default = 'M')

    movie = models.CharField(max_length=100)


    def __str__(self):
        """
        :return:
        """
        return self.name