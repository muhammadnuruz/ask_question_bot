from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "full_name", "is_active", "is_staff", "created_at")
    list_filter = ("is_active", "is_staff", "created_at")
    search_fields = ("username", "full_name")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (_("Asosiy ma'lumotlar"), {
            "fields": ("username", "full_name", "password")
        }),
        (_("Ruxsatlar"), {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        (_("Muhim sanalar"), {
            "fields": ("last_login", "created_at", "updated_at")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "full_name", "password1", "password2"),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ("username",)
        return self.readonly_fields


admin.site.unregister(Group)
