from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    # movie = models.ManyToManyField('Movie', related_name='directors_radsa')

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='filmebi', null=True, blank=True)
    rate = models.FloatField()
    actors = models.ManyToManyField(Actor, related_name='actor_rara')

    def __str__(self):
        return self.name


class Rating(models.Model):
    rate = models.OneToOneField(Movie, on_delete=models.CASCADE)



