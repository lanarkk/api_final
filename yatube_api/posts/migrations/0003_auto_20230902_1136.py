# Generated by Django 3.2.16 on 2023-09-02 08:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20230901_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='posts/', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='UserToFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfollow', to='posts.follow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfollow', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'userfollow',
            },
        ),
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ManyToManyField(related_name='user_to_follow', through='posts.UserToFollow', to=settings.AUTH_USER_MODEL, verbose_name='подписки'),
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
