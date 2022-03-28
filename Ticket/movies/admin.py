from django.contrib import admin
from movies.models import Movie, MovieOption, AttentionList


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieOption)
class MovieOption(admin.ModelAdmin):
    pass


@admin.register(AttentionList)
class AttentionList(admin.ModelAdmin):
    pass
