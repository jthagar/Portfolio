from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about page'),
    path('cv/', views.ceevee, name='cv page'),
    path('hire/', views.hireme, name='hire page'),
    path('projects/', views.projects, name='projects page'),
]
