from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('about/', views.About.as_view(), name = 'about'),
    path('cart/', views.Cart.as_view(), name = 'cart'),
]