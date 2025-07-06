from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from apps.telegram_users.config import get_user_by_chat_id
from bot.buttons.text import adverts, none_advert, forward_advert, back_main_menu, choice_language, choice_language_ru, \
    ask_question, ask_question_en, choice_language_en, ask_question_ru, back_main_menu_en, back_main_menu_ru


async def main_menu_buttons(chat_id: int):
    tg_user = await get_user_by_chat_id(chat_id=chat_id)
    if tg_user.language == 'uz':
        design = [
            [KeyboardButton(text=ask_question)],
            [KeyboardButton(text=choice_language)]
        ]
    elif tg_user.language == "en":
        design = [
            [KeyboardButton(text=ask_question_en)],
            [KeyboardButton(text=choice_language_en)]
        ]
    else:
        design = [
            [KeyboardButton(text=ask_question_ru)],
            [KeyboardButton(text=choice_language_ru)]
        ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_main_menu_button(chat_id: int):
    tg_user = await get_user_by_chat_id(chat_id=chat_id)
    if tg_user.language == 'uz':
        design = [[KeyboardButton(text=back_main_menu)]]
    elif tg_user.language == "en":
        design = [[KeyboardButton(text=back_main_menu_en)]]
    else:
        design = [[KeyboardButton(text=back_main_menu_ru)]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def admin_menu_buttons():
    design = [
        [KeyboardButton(text=adverts)],
        [KeyboardButton(text=back_main_menu)]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def advert_menu_buttons():
    design = [
        [KeyboardButton(text=none_advert), KeyboardButton(text=forward_advert)],
        [KeyboardButton(text=back_main_menu)]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
