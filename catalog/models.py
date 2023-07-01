from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
import locale

# Set the locale to Spanish
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnails')
    description = models.TextField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_thumbnail_url(self):
        return self.thumbnail.url

    def get_absolute_url(self):
        return reverse_lazy('post_detail', args=[str(self.pk)])
    
    def formatted_created_at(self):
        formatted_date = self.created_at.strftime('%d de %B de %Y')
        return formatted_date.capitalize()

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')