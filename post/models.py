from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='post/images/')
    # url = models.URLField(blank=True)

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    watchAgain = models.BooleanField()
    
    def __str__(self):
        return self.text