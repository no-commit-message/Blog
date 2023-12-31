from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False,)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '投稿'
    
    def get_absolute_url(self):
        return reverse_lazy('detail', args=[self.id])