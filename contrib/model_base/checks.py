from django.apps import apps
from django.core.checks import Warning, register


@register()
def check_base_model(**kwargs):
    from contrib.model_base.models import ModelBase

    errors = []
    for app in apps.get_app_configs():

        # skip third party apps
        if app.path.find("site-packages") > -1:
            continue

        for model in app.get_models():
            if not issubclass(model, ModelBase) and not getattr(
                model, "no_model_base", False
            ):
                errors.append(
                    # TODO: When actively used, this should be changed to an Error
                    Warning(
                        "Model does not extend ModelBase",
                        hint="All models should extend from ModelBase or should explicitly set no_mode_base=True",
                        obj=model,
                        id="contrib.model_base.E001",
                    )
                )
        return errors
