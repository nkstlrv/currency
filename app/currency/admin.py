from django.contrib import admin
from currency.models import Rate, ContactUs, Source, RequestResponseLog


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "buy",
        "sell",
        "currency",
        "source",
        "created",
    )
    list_filter = ("currency", ("created"))
    search_fields = (
        "buy",
        "sell",
        "source",
    )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email_from",
        "subject",
        "message",
    )

    search_fields = (
        "id",
        "email_from",
        "subject",
    )

    readonly_fields = (
        "id",
        "email_from",
        "subject",
        "message",
    )

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "url",
    )

    search_fields = (
        "id",
        "name",
    )


@admin.register(RequestResponseLog)
class RequestResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created",
        "method",
        "status_code",
        "path",
        "time",
    )

    list_filter = ("method",)
