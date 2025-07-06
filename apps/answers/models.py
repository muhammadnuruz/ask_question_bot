from django.db import models

from apps.telegram_users.models import TelegramUsers


class Answer(models.Model):
    user = models.ForeignKey(TelegramUsers, on_delete=models.CASCADE, related_name='answers')
    topic = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.full_name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
