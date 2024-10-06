from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(User,  on_delete= models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} and {self.content}"

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.content} and {self.created_at}"
    
