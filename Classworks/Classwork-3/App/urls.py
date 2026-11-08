
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),

    path('actors/', views.actor_list, name='actor_list'),
    path('directors/', views.director_list, name='director_list'),
    path('ratings/', views.rating_list, name='rating_list'),
]
