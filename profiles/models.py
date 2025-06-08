from django.conf import settings
from django.db import models

from contrib.model_base.models import ModelBase


class Profile(ModelBase):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    theme = models.JSONField(default=dict)

    def __str__(self):
        return self.display_name or self.user.username


class Link(ModelBase):
    profile = models.ForeignKey(Profile, related_name="links", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.ImageField(upload_to="link_icons/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-created_at"]
