from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200,verbose_name='')
    last_name = models.CharField(max_length=200,verbose_name='')
    ip = models.CharField(max_length=300,verbose_name='')
    def __str__(self):
        return self.last_name
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='')
    body = models.TextField(verbose_name='')
    author = models.ForeignKey(on_delete=models.CASCADE,verbose_name='',to=User)

