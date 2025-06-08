import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelBase(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    created_at = models.DateTimeField(
        _("created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, editable=False)

    class Meta:
        abstract = True
