from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('nouns/', views.nouns),
    path('verbs/', views.verbs),
    path('vocab_greek/', views.gre_vocab),
    path('vocab_english/', views.eng_vocab)
]
