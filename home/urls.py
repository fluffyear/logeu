from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('nouns/', views.nouns),
    path('verbs/', views.verbs),
    path('vocab/', views.vocab)
]
