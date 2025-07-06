import os
import django
from asgiref.sync import sync_to_async
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AIChatForWork.settings')
django.setup()

from apps.telegram_users.models import TelegramUsers


@sync_to_async
def get_telegram_users():
    return list(TelegramUsers.objects.only('chat_id'))


@sync_to_async
def get_user_by_chat_id(chat_id: int):
    try:
        return TelegramUsers.objects.get(chat_id=chat_id)
    except Exception:
        return None


@sync_to_async
def get_user_by_id(_id: int):
    try:
        return TelegramUsers.objects.get(id=_id)
    except Exception:
        return None


@sync_to_async
def create_user_by_chat_id(chat_id: int, full_name: str, username: str, language: str) -> TelegramUsers:
    user = TelegramUsers.objects.get_or_create(
        chat_id=chat_id,
        defaults={
            "full_name": full_name,
            "username": username,
            "language": language
        }
    )
    return user


@sync_to_async
def update_user_by_chat_id(chat_id: int, language: str) -> TelegramUsers | None:
    user = TelegramUsers.objects.get(chat_id=chat_id)
    user.language = language
    user.save()
    return user


@sync_to_async
def display_user_limit(chat_id: int) -> bool:
    try:
        user = TelegramUsers.objects.get(chat_id=chat_id)
    except TelegramUsers.DoesNotExist:
        return False

    today = timezone.now().date()
    request_count = user.answers.filter(created_at__date=today).count()

    return request_count < 3
