from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('nouns/', views.nouns),
    path('verbs/', views.verbs),
    path('verb_endings_settings/', views.verb_endings_settings),
    path('vocab_greek/', views.gre_vocab),
    path('vocab_english/', views.eng_vocab),
    path('noun_input/', views.noun_input),
    path('vocab_greek_input/', views.gre_vocab_input),
    path('vocab_english_input/', views.eng_vocab_input),
    path('verb_endings/', views.verb_endings),
    path('home/views.update_noun_context', views.update_noun, name="updateNoun"),
    path('home/views.update_verb_context', views.update_verb, name="updateVerb"),
    path('home/views.update_gre_vocab_context', views.update_gre_vocab, name="updateGreVocab"),
    path('home/views.update_eng_vocab_context', views.update_eng_vocab, name="updateEngVocab"),
    path('home/views.update_noun_input_context', views.update_noun_input, name="updateNounInput"),
    path('home/views.update_gre_vocab_input_context', views.update_gre_vocab_input, name="updateGreVocabInput"),
    path('home/views.update_eng_vocab_input_context', views.update_eng_vocab_input, name="updateEngVocabInput"),
    path('home/views.update_verb_endings_context', views.update_verb_endings, name="updateVerbEndings"),
    path('home/views.post_update_verb_endings_context', views.post_update_verb_endings, name="updateVerbEndingsPOST")
]
