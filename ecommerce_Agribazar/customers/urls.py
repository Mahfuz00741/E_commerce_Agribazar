from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name = 'login'),
    path('signup/', views.Signup.as_view(), name = 'signup'),
    path('logout', views.logout.as_view(), name = 'logout'),
]
