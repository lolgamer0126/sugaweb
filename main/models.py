from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
