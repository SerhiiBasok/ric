from django.contrib import admin
from django.urls import path

from characters.views import get_random_character

urlpatterns = [
    path("charakters/random/", get_random_character, ),
]

app_name = "characters"