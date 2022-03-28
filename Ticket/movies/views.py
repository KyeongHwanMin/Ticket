from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieDetailSerializer


class MovieDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

