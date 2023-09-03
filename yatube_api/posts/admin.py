from django.contrib import admin

from .models import Comment, Group, Post, Follow


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Модель Группы в админ зоне.
    Описывает ее внешний вид и функционал."""

    list_display = (
        'title',
        'slug',
        'description',
    )
    search_fields = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Модель Поста в админ зоне.
    Описывает ее внешний вид и функционал."""

    list_display = (
        'text',
        'pub_date',
        'author',
        'image',
        'group',
    )
    search_fields = ('text', 'author',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Модель Комментария в админ зоне.
    Описывает ее внешний вид и функционал."""

    list_display = (
        'author',
        'post',
        'text',
        'created',
    )
    search_fields = ('text', 'post', 'author',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Модель Подписки в админ зоне.
    Описывает ее внешний вид и функционал."""

    list_display = (
        'user',
        'following',
    )
    search_fields = ('user', 'following',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'
