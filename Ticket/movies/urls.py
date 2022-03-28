from django.urls import path
from movies.views import MovieDetailView

urlpatterns = [
    path('api/v1/movies/', MovieDetailView.as_view()),
]
