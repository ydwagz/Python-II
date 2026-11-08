
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Avg

from .models import Movie, Actor, Director, Rating


def dashboard(request):
    context = {
        'movies': Movie.objects.select_related('author').order_by('-id')[:6],
        'actors': Actor.objects.order_by('-id')[:6],
        'directors': Director.objects.order_by('-id')[:6],
        'movie_count': Movie.objects.count(),
        'actor_count': Actor.objects.count(),
        'director_count': Director.objects.count(),
        'rating_count': Rating.objects.count(),
        'average_rating': Movie.objects.aggregate(avg=Avg('rate'))['avg'],
    }
    return render(request, 'movies/dashboard.html', context)


def movie_list(request):
    movies = Movie.objects.select_related('author').prefetch_related('actors')

    return render(request, 'movies/movie_list.html', {
        'movies': movies
    })


def movie_detail(request, pk):
    movie = get_object_or_404(
        Movie.objects.select_related('author').prefetch_related('actors'),
        pk=pk
    )

    return render(request, 'movies/movie_detail.html', {
        'movie': movie
    })


def actor_list(request):
    actors = Actor.objects.annotate(
        movie_count=Count('actor_rara', distinct=True)
    ).prefetch_related('actor_rara')

    return render(request, 'movies/actor_list.html', {
        'actors': actors
    })


def director_list(request):
    directors = Director.objects.annotate(
        movie_count=Count('filmebi', distinct=True)
    ).prefetch_related('filmebi')

    return render(request, 'movies/director_list.html', {
        'directors': directors
    })


def rating_list(request):
    ratings = Rating.objects.select_related(
        'rate', 'rate__author'
    ).prefetch_related('rate__actors')

    return render(request, 'movies/rating_list.html', {
        'ratings': ratings
    })
