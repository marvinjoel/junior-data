from django.db import models


class SocialMedia(models.Model):
    github = models.CharField(max_length=200)
    gitlab = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    web = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedias'
        ordering = ['id']