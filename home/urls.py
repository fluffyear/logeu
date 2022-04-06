from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('nouns/', views.nouns),
    path('verbs/', views.verbs),
    path('vocab_greek/', views.gre_vocab),
    path('vocab_english/', views.eng_vocab),
    path('noun_input/', views.noun_input),
    path('vocab_greek_input/', views.gre_vocab_input),
    path('vocab_english_input/', views.eng_vocab_input)
]
