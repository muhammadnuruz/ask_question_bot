from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from apps.answers.config import create_answer
from apps.telegram_users.config import display_user_limit, get_user_by_chat_id
from bot.ask_question import ask_question_function
from bot.buttons.reply_buttons import back_main_menu_button, main_menu_buttons
from bot.buttons.text import ask_question, ask_question_en, ask_question_ru
from bot.states import AskQuestion

router = Router()


@router.message(F.text.in_([ask_question, ask_question_en, ask_question_ru]))
async def ask_question_function_1(msg: Message, state: FSMContext):
    limit = await display_user_limit(chat_id=msg.from_user.id)
    if not limit:
        if msg.text == ask_question:
            await msg.answer("Bugungi limitingiz tugagan!", reply_markup=await main_menu_buttons(msg.from_user.id))
        elif msg.text == ask_question_en:
            await msg.answer("Your limit for today has expired!",
                             reply_markup=await main_menu_buttons(msg.from_user.id))
        else:
            await msg.answer("Ваш лимит на сегодня истек!", reply_markup=await main_menu_buttons(msg.from_user.id))
        return

    if msg.text == ask_question:
        await msg.answer("Qaysi mavzu bo‘yicha savolingiz bor? 😊",
                         reply_markup=await back_main_menu_button(msg.from_user.id))
    elif msg.text == ask_question_en:
        await msg.answer("What is your question topic? 😊", reply_markup=await back_main_menu_button(msg.from_user.id))
    else:
        await msg.answer("По какой теме у вас вопрос? 😊", reply_markup=await back_main_menu_button(msg.from_user.id))
    await state.set_state(AskQuestion.topic)


@router.message(AskQuestion.topic)
async def ask_question_function_2(msg: Message, state: FSMContext):
    await state.update_data(topic=msg.text)
    await msg.answer("Savolingizni yuboring 😊", reply_markup=await back_main_menu_button(msg.from_user.id))
    await state.set_state(AskQuestion.question)


@router.message(AskQuestion.question)
async def ask_question_function_3(msg: Message, state: FSMContext):
    data = await state.get_data()
    topic = data.get("topic")
    await state.clear()

    tg_user = await get_user_by_chat_id(msg.from_user.id)

    if tg_user.language == 'uz':
        system_msg = f"Foydalanuvchilarga {topic} bo'yicha yordamchisan. Javobni aniq qil."
    elif tg_user.language == 'en':
        system_msg = f"You are helping users with {topic}. Please clarify your answer."
    else:
        system_msg = f"Вы помогаете пользователям с {topic}. Пожалуйста, уточните свой ответ."

    try:
        result = ask_question_function(system_msg, msg.text)
        await msg.answer(result, reply_markup=await main_menu_buttons(msg.from_user.id))
        await create_answer(user=tg_user, topic=topic, question=msg.text, answer=result)
    except Exception as e:
        await msg.answer(str(e))
