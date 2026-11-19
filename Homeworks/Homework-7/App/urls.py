from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]