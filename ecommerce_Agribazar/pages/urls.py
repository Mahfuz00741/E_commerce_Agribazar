from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.Login.as_view(), name = 'login'),
    path('signup/', views.Signup.as_view(), name = 'signup'),
    path('about/', views.About.as_view(), name = 'about'),
]
