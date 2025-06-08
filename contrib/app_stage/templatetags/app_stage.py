from django import template
from django.conf import settings

from contrib.app_stage.constants import AppStage
from contrib.app_stage.utils import GitHash

register = template.Library()


git_hash = GitHash()


@register.inclusion_tag("app_stage/app_stage_labels.html")
def render_app_stage():
    if settings.APP_STAGE not in [AppStage.DEVELOPMENT, AppStage.STAGING]:
        return {"show_app_stage_labels": False}

    return {
        "show_app_stage_labels": True,
        "stage": settings.APP_STAGE.value,
        "git_hash": git_hash.get_current(),
    }
