from django.urls import path

from . import views

urlpatterns = [
    path("genre/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
