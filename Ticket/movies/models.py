from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='영화제목')
    year = models.PositiveIntegerField(default=0, verbose_name='제작년도')
    original_title = models.CharField(max_length=100, null=True, verbose_name="원제")
    video_url1 = models.URLField(null=True, verbose_name='영상주소')
    video_url2 = models.URLField(null=True, verbose_name='영상주소')
    video_url3 = models.URLField(null=True, verbose_name='영상주소')
    video_url4 = models.URLField(null=True, verbose_name='영상주소')
    cast = models.CharField(max_length=100, verbose_name='출연진')
    synopsis = models.TextField(verbose_name='시놉시스')
    image = models.ImageField(default='media/', verbose_name='포스터')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Movie'


class MovieOption(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_option')
    genre = models.CharField(max_length=100, verbose_name="장르")
    grade = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],
        verbose_name="평점"
    )
    runningtime = models.CharField(max_length=100, verbose_name="재생시간")
    director = models.CharField(max_length=100, verbose_name="감독")

    class Meta:
        db_table = 'MovieOption'

    def __str__(self):
        return f'{self.movie.name}_기본정보'


class AttentionList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user')
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='movie_Attention_list')
    is_watchlist = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)
    is_like = models.BooleanField(default=False)
    is_dislike = models.BooleanField(default=False)

    class Meta:
        db_table = 'AttentionList'

    def __str__(self):
        return f'관심목록'
