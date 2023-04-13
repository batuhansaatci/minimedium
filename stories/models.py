from django.db import models

# Create your models here.

class Story(models.Model):

    author = models.CharField(max_length=200)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    content = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    released_at =models.DateField()

    def __str__(self):
        return self.title