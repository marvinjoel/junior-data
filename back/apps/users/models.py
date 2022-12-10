from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

from apps.info.models import SocialMedia
from apps.users.manager import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):

    ROL_CHOICES = [
        ('Full-Stack', 'Full-Stack'),
        ('Front-End', 'Front-End'),
        ('Back-End', 'Back-End'),
        ('UX-UI', 'UX-UI'),
        ('Mobile', 'Mobile'),
        ('DevOps', 'DevOps'),
    ]

    username = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    avatar = models.ImageField(default="no-avatar.jpg", upload_to='image/users', null=True, blank=True)
    rol = models.CharField(choices=ROL_CHOICES, max_length=11)
    social = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token)
    #     }
