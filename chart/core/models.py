from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    name = models.CharField(max_length=50)
    meaning = models.TextField()
    
    def __str__(self):
        return self.name