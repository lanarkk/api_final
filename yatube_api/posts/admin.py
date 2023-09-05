from django.contrib import admin

from posts.models import Comment, Follow, Group, Post


admin.site.empty_value_display = '-пусто-'

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
