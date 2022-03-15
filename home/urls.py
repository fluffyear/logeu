from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('nouns/', views.nouns),
    path('verbs/answer/', views.v_answer),
    path('verbs/', views.verbs)
]