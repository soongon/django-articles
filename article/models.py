from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title
