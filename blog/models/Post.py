from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='name'
    )
    last_name = models.CharField(max_length=200,
                                 verbose_name='last name'
                                 )
    ip = models.CharField(
        max_length=300,
        verbose_name='ip'
    )

    def __str__(self):
        return self.last_name


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='title'
    )
    body = models.TextField(
        verbose_name='body'
    )
    author = models.ForeignKey(
        on_delete=models.CASCADE,
        verbose_name='user',
        to=User
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            args=[str(self.id)]
        )
