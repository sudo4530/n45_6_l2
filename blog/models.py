from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=True)
    description = models.TextField(null=False)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.author}"


class Book(models.Model):
    name = models.CharField()
    description = models.TextField()
    author = models.CharField(max_length=100)
    price = models.FloatField()
    count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
