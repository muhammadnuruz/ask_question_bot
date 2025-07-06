from django.contrib import admin
from apps.answers.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'topic', 'created_at', 'updated_at')
    list_filter = ('created_at', 'user')
    search_fields = ('topic', 'question', 'answer')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    autocomplete_fields = ('user',)
