from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)

    published_date = models.DateTimeField(null=True, blank=True)

    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title