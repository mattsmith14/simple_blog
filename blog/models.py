from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)

    published_date = models.DateTimeField(null=True, blank=True)

    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"id": self.pk})