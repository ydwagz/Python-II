
from django.shortcuts import render, get_object_or_404
from .models import Movie, Actor, Director, Rating


def dashboard(request):
    movies = Movie.objects.select_related(
        'author'
    ).prefetch_related('actors').all()

    actors = Actor.objects.prefetch_related('actor_rara').all()
    directors = Director.objects.prefetch_related('filmebi').all()
    ratings = Rating.objects.select_related('rate').all()

    context = {
        'movies': movies,
        'actors': actors,
        'directors': directors,
        'ratings': ratings,
        'movie_count': movies.count(),
        'actor_count': actors.count(),
        'director_count': directors.count(),
        'rating_count': ratings.count(),
    }

    return render(request, 'movies/dashboard.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(
        Movie.objects.select_related('author').prefetch_related('actors'),
        pk=pk
    )

    return render(request, 'movies/movie_detail.html', {
        'movie': movie
    })
