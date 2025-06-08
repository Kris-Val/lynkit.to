import re
from itertools import chain

from django.contrib import admin
from django.contrib.admin.utils import NotRelationField, get_fields_from_path
from django.core.checks import Error
from django.core.exceptions import FieldDoesNotExist
from django.db.models.fields.related import RelatedField


def check_search_fields(obj):
    """
    Check that search_fields only contains fields or usable attributes.
    django.contrib.admin.checks._check_search_fields only verifies that
    the field is a list or a tuple.

    code is based on
        - django.contrib.admin.checks._check_list_filter
        - django.contrib.admin.checks._check_list_display
    """
    return list(
        chain.from_iterable(
            check_search_fields_item(obj, item, "search_fields[%d]" % index)
            for index, item in enumerate(obj.search_fields)
        )
    )


def check_search_fields_item(obj, item, label):
    if callable(item):
        return []

    if hasattr(obj, item):
        return []

    field = item

    # Since the search lookup type can be specified, remove it before the relation check
    field = re.sub("__exact", "", field)
    field = re.sub("__iexact", "", field)
    field = re.sub("__contains", "", field)
    field = re.sub("__icontains", "", field)
    field = re.sub("__startswith", "", field)
    field = re.sub("__istartswith", "", field)
    field = re.sub("__endswith", "", field)
    field = re.sub("__iendswith", "", field)

    try:
        # can possibly have relationships (e.g. 'field__rel')
        fields = get_fields_from_path(obj.model, field)

        # the last field should not be a FK (not searchable)
        if isinstance(fields[-1], RelatedField):
            return [
                Error(
                    "The value of '%s' refers to '%s', which is a Foreign Key."
                    % (label, item),
                    obj=obj.__class__,
                    id="contrib.admin_site.E003",
                )
            ]
    except (NotRelationField, FieldDoesNotExist):
        return [
            Error(
                "The value of '%s' refers to '%s', which does not refer to a Field."
                % (label, field),
                obj=obj.__class__,
                id="contrib.admin_site.E001",
            )
        ]
    return []


def check_list_select_related(obj):
    """
    Check that list_select_related only contains fields or usable attributes.
    django.contrib.admin.checks._check_list_select_related only verifies that
    the field is a boolean, list or a tuple.

    code is based on
        - django.contrib.admin.checks._check_list_filter
        - django.contrib.admin.checks._check_list_display
    """
    if type(obj.list_select_related) is bool:
        return []

    return list(
        chain.from_iterable(
            check_list_select_related_item(obj, item, "list_select_related[%d]" % index)
            for index, item in enumerate(obj.list_select_related)
        )
    )


def check_list_select_related_item(obj, item, label):
    if callable(item):
        return []

    if hasattr(obj, item):
        return []

    field = item

    try:
        # can possibly have relationships (e.g. 'field__rel')
        get_fields_from_path(obj.model, field)
    except (NotRelationField, FieldDoesNotExist):
        return [
            Error(
                "The value of '%s' refers to '%s', which does not refer to a Field."
                % (label, field),
                obj=obj.__class__,
                id="contrib.admin_site.E002",
            )
        ]
    return []


def check_admin_site_models(app_configs, **kwargs):
    """
    These checks are an extension on the admin checks from Django itself.
    For some reason, they chose to not verify some settings for model validity,
      so we will do that here.
    """

    errors = []
    for a_model, a_site in admin.site._registry.items():
        if isinstance(a_site, admin.ModelAdmin):
            errors += check_search_fields(a_site)
            errors += check_list_select_related(a_site)
    return errors
