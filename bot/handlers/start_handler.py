from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from apps.telegram_users.config import get_user_by_chat_id, create_user_by_chat_id, update_user_by_chat_id
from bot.buttons.inline_buttons import language_buttons
from bot.buttons.reply_buttons import main_menu_buttons
from bot.buttons.text import back_main_menu, choice_language, choice_language_ru, choice_language_en, back_main_menu_en, \
    back_main_menu_ru
from aiogram.fsm.context import FSMContext

from bot.dispatcher import bot
from bot.states import RegState

admins = [1974800905, 169839849]

router = Router()


@router.message(F.text.in_([back_main_menu, back_main_menu_en, back_main_menu_ru]))
async def back_main_menu_msg(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(msg.text, reply_markup=await main_menu_buttons(msg.from_user.id))


@router.message(CommandStart())
async def start_function(msg: Message, state: FSMContext):
    user = await get_user_by_chat_id(msg.from_user.id)
    if user:
        if user.language == 'uz':
            await msg.answer("♻️ Bot yangilandi", reply_markup=await main_menu_buttons(msg.from_user.id))
        elif user.language == "en":
            await msg.answer("♻️ Bot updated", reply_markup=await main_menu_buttons(msg.from_user.id))
        else:
            await msg.answer("♻️ Бот обновлен", reply_markup=await main_menu_buttons(msg.from_user.id))
    else:
        await state.set_state(RegState.language)
        await msg.answer("""
Tilni tanlang

-------------

Выберите язык

-------------

Choose language""", reply_markup=await language_buttons())


@router.callback_query(RegState.language)
async def choose_language(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    language = call.data.split("_")[-1]
    for admin in admins:
        await bot.send_message(chat_id=admin, text=f"""
Yangi user🆕
ID: <a href='tg://user?id={call.from_user.id}'>{call.from_user.id}</a>
Username: @{call.from_user.username}
Ism-Familiya: {call.from_user.full_name}
Til: {language}""", parse_mode='HTML')
    await create_user_by_chat_id(
        chat_id=call.from_user.id,
        full_name=call.from_user.full_name,
        username=call.from_user.username,
        language=language)
    if language == 'uz':
        await call.message.answer(text="Hush kelibsiz 😊", reply_markup=await main_menu_buttons(call.from_user.id))
    elif language == 'en':
        await call.message.answer(text="Welcome 😊", reply_markup=await main_menu_buttons(call.from_user.id))
    else:
        await call.message.answer(text="Добро пожаловать 😊", reply_markup=await main_menu_buttons(call.from_user.id))
    await state.clear()


@router.message(F.text.in_([choice_language, choice_language_en, choice_language_ru]))
async def change_language_prompt(msg: Message):
    await msg.answer(
        text="""
Tilni tanlang

-------------

Выберите язык

-------------

Choose language""",
        reply_markup=await language_buttons())


@router.callback_query(F.data.startswith('language_'))
async def update_language(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.delete()
    language = call.data.split("_")[-1]
    await update_user_by_chat_id(chat_id=call.from_user.id, language=language)
    if language == 'uz':
        await call.message.answer("🇺🇿 Til o‘zgartirildi", reply_markup=await main_menu_buttons(call.from_user.id))
    elif language == 'en':
        await call.message.answer("🇬🇧 Language updated", reply_markup=await main_menu_buttons(call.from_user.id))
    else:
        await call.message.answer("🇷🇺 Язык изменен", reply_markup=await main_menu_buttons(call.from_user.id))
