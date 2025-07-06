from django.contrib import admin
from apps.telegram_users.models import TelegramUsers


@admin.register(TelegramUsers)
class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "username", "language", "created_at", "updated_at")
    list_filter = ("created_at", "language")
    search_fields = ("full_name", "username", "chat_id")
    readonly_fields = ("created_at", "updated_at", "chat_id")
    ordering = ("-created_at",)
