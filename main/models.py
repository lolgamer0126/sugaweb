from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse 
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = RichTextField(null=False, blank=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self): # new
        return reverse('detail', args=[str(self.id)])