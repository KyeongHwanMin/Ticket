from django.urls import path
from movies.views import MovieDetailView, MovieView

urlpatterns = [
    path('api/v1/movies/', MovieView.as_view()),
    path('api/v1/movies/<int:pk>/', MovieDetailView.as_view()),
]
