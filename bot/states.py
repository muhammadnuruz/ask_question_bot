from aiogram.fsm.state import StatesGroup, State


class AskQuestion(StatesGroup):
    topic = State()
    question = State()


class RegState(StatesGroup):
    language = State()


class AdminState(StatesGroup):
    advert = State()
    send_forward = State()


class AskQuestionState(StatesGroup):
    question = State()
