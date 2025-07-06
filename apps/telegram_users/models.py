from django.db import models
from django.utils import timezone


class TelegramUsers(models.Model):
    LANGUAGE_CHOICES = [
        ('uz', 'O‘zbek'),
        ('ru', 'Русский'),
        ('en', 'English'),
    ]
    chat_id = models.CharField(max_length=250, unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def requests_count(self):
        today = timezone.now().date()
        return self.requests.filter(created_at__date=today).count()

    def requests_count_2(self):
        return self.requests_count() < 3

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Telegram user"
        verbose_name_plural = "Telegram users"
