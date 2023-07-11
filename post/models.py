from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from io import BytesIO
import io
from django.core.files import File
import os
from django.dispatch import receiver

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='post/images/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        pil_image = Image.open(self.image)
        format = pil_image.format

        if self.image:
            if format == 'PNG':
                output = io.BytesIO()
                pil_image.save(output, format='PNG', optimize=True)
                output.seek(0)
                self.image = File(output, name=self.image.name)
            
            elif format == 'JPEG':
                output = io.BytesIO()
                pil_image.save(output, format='JPEG', quality=50)
                output.seek(0)
                self.image = File(output, name=self.image.name)

        super(Post, self).save(*args, **kwargs)

@receiver(models.signals.pre_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    if instance.image:
        file_path = instance.image.path
        if os.path.exists(file_path):
            os.remove(file_path)

class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.text