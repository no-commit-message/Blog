from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False,)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '投稿'