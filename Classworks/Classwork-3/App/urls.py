from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
]
