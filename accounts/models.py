from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
from django.contrib.auth.models import User
from your_app_name.models import UserProfile

for user in User.objects.all():
    UserProfile.objects.get_or_create(user=user)
"""

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', blank=True) 
    email = models.EmailField(max_length=150, blank=True)
    signature = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
