from django.contrib import admin
from django.core.checks import Error
from django.db import models
from django.test import TestCase

from .checks import check_list_select_related, check_search_fields


class TestModelRelatedInfo(models.Model):
    title = models.CharField("title", max_length=255)


class TestModel(models.Model):
    title = models.CharField("title", max_length=255)

    info = models.ForeignKey(TestModelRelatedInfo, on_delete=models.PROTECT)


class TestModelAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_select_related = ("title",)


class CheckAdminSiteModelsTests(TestCase):
    def test_search_fields_field_no_field(self):
        test_model_admin = TestModelAdmin(model=TestModel, admin_site=None)
        test_model_admin.search_fields = ("typo",)
        errors = check_search_fields(test_model_admin)
        expected_errors = [
            Error(
                "The value of 'search_fields[0]' refers to 'typo',"
                " which does not refer to a Field.",
                hint=None,
                obj=TestModelAdmin,
                id="contrib.admin_site.E001",
            )
        ]
        self.assertEqual(errors, expected_errors)

    def test_search_fields_field_no_relation_field(self):
        test_model_admin = TestModelAdmin(model=TestModel, admin_site=None)

        # Add existing relation to verify it is allowed
        test_model_admin.search_fields = ("info__typo", "info__title")
        errors = check_search_fields(test_model_admin)
        expected_errors = [
            Error(
                "The value of 'search_fields[0]' refers to 'info__typo',"
                " which does not refer to a Field.",
                hint=None,
                obj=TestModelAdmin,
                id="contrib.admin_site.E001",
            )
        ]
        self.assertEqual(errors, expected_errors)

    def test_search_fields_field_is_related_field(self):
        test_model_admin = TestModelAdmin(model=TestModel, admin_site=None)

        # Add existing relation to verify it is allowed
        test_model_admin.search_fields = ("info",)
        errors = check_search_fields(test_model_admin)
        expected_errors = [
            Error(
                "The value of 'search_fields[0]' refers to 'info',"
                " which is a Foreign Key.",
                hint=None,
                obj=TestModelAdmin,
                id="contrib.admin_site.E003",
            )
        ]
        self.assertEqual(errors, expected_errors)

    def test_search_fields_field_search_type_allowed(self):
        test_model_admin = TestModelAdmin(model=TestModel, admin_site=None)
        test_model_admin.search_fields = (
            "info__title__exact",
            "info__title__iexact",
            "info__title__contains",
            "info__title__icontains",
            "info__title__startswith",
            "info__title__istartswith",
            "info__title__endswith",
            "info__title__iendswith",
        )
        errors = check_search_fields(test_model_admin)
        expected_errors = []
        self.assertEqual(errors, expected_errors)

    def test_list_select_related_no_field(self):
        test_model_admin = TestModelAdmin(model=TestModel, admin_site=None)
        test_model_admin.list_select_related = ("lsr_typo",)
        errors = check_list_select_related(test_model_admin)
        expected_errors = [
            Error(
                "The value of 'list_select_related[0]' refers to 'lsr_typo',"
                " which does not refer to a Field.",
                hint=None,
                obj=TestModelAdmin,
                id="contrib.admin_site.E002",
            )
        ]
        self.assertEqual(errors, expected_errors)

    def test_list_select_related_no_relation_field(self):
        test_model_admin = TestModelAdmin(model=TestModel, admin_site=None)

        # Add existing relation to verify it is allowed
        test_model_admin.list_select_related = ("info__lsr_typo", "info__title")
        errors = check_list_select_related(test_model_admin)
        expected_errors = [
            Error(
                "The value of 'list_select_related[0]' refers to 'info__lsr_typo',"
                " which does not refer to a Field.",
                hint=None,
                obj=TestModelAdmin,
                id="contrib.admin_site.E002",
            )
        ]
        self.assertEqual(errors, expected_errors)
