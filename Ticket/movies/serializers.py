from rest_framework.serializers import ModelSerializer
from movies.models import Movie, MovieOption, AttentionList


class MovieDefaultSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieOptionSerializer(ModelSerializer):
    class Meta:
        model = MovieOption
        fields = [
            'id',
            'grade',
            'genre',
            'runningtime',
            'director',
        ]


class AttentionListSerializer(ModelSerializer):
    class Meta:
        model = AttentionList
        fields = [
            'is_watchlist',
            'is_seen',
            'is_like',
            'is_dislike',
        ]


class MovieDetailSerializer(ModelSerializer):
    movie_option = MovieOptionSerializer(many=True, read_only=True)
    movie_Attention_list = AttentionListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            'name',
            'year',
            'original_title',
            'video_url1',
            'video_url2',
            'video_url3',
            'video_url4',
            'cast',
            'synopsis',
            'image',
            'movie_option',
            'movie_Attention_list',
        ]

