from django.urls import path, include
from movies.views import MovieDetailView, MovieView, AttentionListView, AttentionDetailView

urlpatterns = [
    path('api/v1/movies/', MovieView.as_view()),
    path('api/v1/movies/<int:pk>/', MovieDetailView.as_view()),
    path('api/v1/attentionlist/', AttentionListView.as_view()),
    path('api/v1/attentionlist/<int:pk>', AttentionDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

