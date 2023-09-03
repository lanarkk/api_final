from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

NUMBER_OF_LETTERS_VISIBLE = 21


class Group(models.Model):
    """Модель группы. Создаёт
    в бд таблицу с группами."""

    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return self.title[:NUMBER_OF_LETTERS_VISIBLE]


class Post(models.Model):
    """Модель поста. Создает в бд
    таблицу с постами пользователей."""

    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        null=True,
        default=None,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа',
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        default_related_name = "posts"
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:NUMBER_OF_LETTERS_VISIBLE]


class Comment(models.Model):
    """Модель комментария. Создает
    в бд таблицу с комментариями."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
    )
    text = models.TextField('Текст')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        default_related_name = "comments"
        ordering = ('-created',)

    def __str__(self):
        return self.text[:NUMBER_OF_LETTERS_VISIBLE]


class Follow(models.Model):
    """Модель Подписки. Создает
    в бд таблицу с подписками."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_following"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_to_follow"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_following'
            ),
            models.CheckConstraint(
                name='prevent_self_follow',
                check=~models.Q(user=models.F("following")),
            ),
        ]
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f'{self.user} following {self.following}'
