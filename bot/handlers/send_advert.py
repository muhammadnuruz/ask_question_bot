import asyncio
from aiogram import Router, F
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter

from apps.telegram_users.config import get_telegram_users
from bot.buttons.reply_buttons import (
    main_menu_buttons, back_main_menu_button,
    advert_menu_buttons, admin_menu_buttons
)
from bot.buttons.text import adverts, none_advert, forward_advert
from bot.handlers import admins
from bot.states import AdminState

router = Router()


@router.message(Command("admin"))
async def send_message_function_1(msg: Message):
    if msg.from_user.id in admins:
        await msg.answer("👨‍💼 Admin menyusiga xush kelibsiz!", reply_markup=await admin_menu_buttons())


@router.message(F.text == adverts)
async def send_message_function_2(msg: Message):
    if msg.from_user.id in admins:
        await msg.answer("📝 Reklama formatini tanlang:", reply_markup=await advert_menu_buttons())


@router.message(F.text == none_advert)
async def send_message_function_3(msg: Message, state: FSMContext):
    if msg.from_user.id in admins:
        await state.set_state(AdminState.advert)
        await msg.answer(
            "✉️ Reklamani yuboring:",
            reply_markup=await back_main_menu_button(msg.from_user.id)
        )


@router.message(AdminState.advert)
async def send_message_function_4(msg: Message, state: FSMContext):
    await state.clear()
    users = await get_telegram_users()
    sent = 0
    failed = 0
    status_msg = await msg.answer("⏳ Reklama yuborilmoqda...")
    for user in users:
        try:
            await msg.copy_to(
                chat_id=int(user.chat_id),
                caption=msg.caption,
                caption_entities=msg.caption_entities,
                reply_markup=msg.reply_markup
            )
            sent += 1
            await asyncio.sleep(0.1)
        except Exception:
            failed += 1
    await status_msg.delete()
    await msg.answer(f"""📢 Reklama tarqatildi

📬 Yetkazildi: {sent} ta foydalanuvchiga
❌ Yetkazilmadi: {failed} ta foydalanuvchiga""", reply_markup=await main_menu_buttons(msg.from_user.id))


@router.message(F.text == forward_advert)
async def send_message_function_5(msg: Message, state: FSMContext):
    if msg.from_user.id in admins:
        await state.set_state(AdminState.send_forward)
        await msg.answer("🔁 Forward xabarni yuboring:",
                         reply_markup=await back_main_menu_button(msg.from_user.id))


@router.message(AdminState.send_forward)
async def send_message_function_6(msg: Message, state: FSMContext):
    await state.clear()
    users = await get_telegram_users()
    sent = 0
    failed = 0
    status_msg = await msg.answer("⏳ Xabar forward qilinmoqda...")
    for user in users:
        try:
            await msg.bot.forward_message(
                chat_id=int(user.chat_id),
                from_chat_id=msg.chat.id,
                message_id=msg.message_id
            )
            sent += 1
            await asyncio.sleep(0.05)
        except Exception:
            failed += 1
    await status_msg.delete()
    await msg.answer(f"""📤 Forward xabar tarqatildi

📬 Yetkazildi: {sent} ta foydalanuvchiga
❌ Yetkazilmadi: {failed} ta foydalanuvchiga""", reply_markup=await main_menu_buttons(msg.from_user.id))
