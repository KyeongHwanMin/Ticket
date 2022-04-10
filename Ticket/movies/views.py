from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie, AttentionList
from movies.permissions import IsAdminOrReadOnly, IsUser
from movies.serializers import MovieDetailSerializer, MovieDefaultSerializer, AttentionListSerializer


class MovieView(APIView):
    def get(self, request):
        qs = Movie.objects.all()
        if qs.exists():
            serializer = MovieDefaultSerializer(qs, many=True)
            return Response(serializer.data)
        return Response({'message': 'Object Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)

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
        if Movie is not None:
            serializer = MovieDetailSerializer(Movie)
            return Response(serializer.data)
        return Response({'message': 'Object Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)

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


class AttentionListView(APIView):

    def post(self, request):
        user_id = self.request.user.id
        movie_id = request.data['movie_id']
        if AttentionList.objects.filter(movie_id=movie_id).exists():
            return Response(data={'error': '이미 존재하는 관심목록 입니다.'}, status=status.HTTP_409_CONFLICT)

        serializer = AttentionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id, movie_id=movie_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AttentionDetailView(APIView):
    permission_classes = [IsUser]

    def get_object(self, pk):
        try:
            qs = AttentionList.objects.get(pk=pk)
            self.check_object_permissions(self.request, qs)
            return qs
        except ObjectDoesNotExist:
            return None

    def get(self, request, pk):
        attentionlist = self.get_object(pk)
        if attentionlist is not None:
            serializer = AttentionListSerializer(attentionlist)
            return Response(serializer.data)
        return Response({'message': 'Object Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        attentionlist = self.get_object(pk)
        serializer = AttentionListSerializer(attentionlist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, statu=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attentionlist = self.get_object(pk)
        attentionlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
