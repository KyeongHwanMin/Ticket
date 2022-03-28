from rest_framework.serializers import ModelSerializer
from movies.models import Movie, MovieOption, AttentionList


class MovieDefaultSerializer(ModelSerializer):
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
        ]


class MovieOption(ModelSerializer):
    class Meta:
        model = MovieOption
        fields = [
            'movie',
            'grade',
            'genre',
            'runningtime',
            'director',
        ]


class AttentionList(ModelSerializer):
    class Meta:
        model = AttentionList
        fields = [
            'is_watchlist',
            'is_seen',
            'is_like',
            'is_dislike',
        ]


class MovieDetailSerializer(ModelSerializer):
    movie_option = MovieOption(many=True, read_only=True)
    movie_Attention_list = AttentionList(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = MovieDefaultSerializer.Meta.fields + [
            'movie_option',
            'movie_Attention_list'
        ]
