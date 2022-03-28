from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.permissions import IsAdminOrReadOnly
from movies.serializers import MovieDetailSerializer, MovieDefaultSerializer


class MovieView(APIView):
    def get(self, request):
        qs = Movie.objects.all()
        serializer = MovieDefaultSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_superuser:
            serializer = MovieDefaultSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class MovieDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            qs = Movie.objects.get(pk=pk)
            self.check_object_permissions(self.request, qs)
            return qs
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk):
        Movie = self.get_object(pk)
        serializer = MovieDetailSerializer(Movie)
        return Response(serializer.data)

    def patch(self, request, pk):
        Movie = self.get_object(pk)
        if Movie is not None:
            serializer = MovieDetailSerializer(Movie, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response({'message': 'Object Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        Movie = self.get_object(pk)
        if Movie is not None:
            Movie.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response({'message': 'Object Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)




