from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='media/thumbnails')
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_thumbnail_url(self):
        return self.thumbnail.url

    def get_absolute_url(self):
        return reverse_lazy('post_detail', args=[str(self.pk)])
