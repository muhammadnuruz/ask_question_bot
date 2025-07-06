from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv('TOKEN')


bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()
