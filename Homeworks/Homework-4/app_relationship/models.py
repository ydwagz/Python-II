from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.DateField()
    genre = models.CharField(max_length=50)
    actors = models.ManyToManyField('Actors', related_name='movies')

    def __str__(self):
        return self.title

class Actors(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class directors(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movies, related_name='directors')

    def __str__(self):
        return self.name
    