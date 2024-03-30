from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CustomUser(User):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=(('M', 'Male'),
                                                       ('F', 'Female'),
                                                       ('O', 'Other')))


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars', default='avatars/default.png')
    bio = models.TextField(max_length=500, blank=True)
    joined_date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f'Profile for user {self.user.username}'
