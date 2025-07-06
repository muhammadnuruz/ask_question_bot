import os
import django
from asgiref.sync import sync_to_async

from apps.telegram_users.models import TelegramUsers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AIChatForWork.settings')
django.setup()

from apps.answers.models import Answer


@sync_to_async
def create_answer(user: TelegramUsers, question: str, answer: str, topic: str) -> Answer | None:
    try:
        new_answer = Answer.objects.create(
            user=user,
            topic=topic,
            question=question,
            answer=answer
        )
        return new_answer
    except Exception:
        return None
