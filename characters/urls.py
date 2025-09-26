from django.contrib import admin
from django.urls import path

from characters.views import get_random_character, CharacterListView

urlpatterns = [
    path("charakters/random/", get_random_character, name="characters-random"),
    path("charakters/", CharacterListView.as_view(), name="characters" ),
]

app_name = "characters"