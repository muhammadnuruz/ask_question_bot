import asyncio

from bot.dispatcher import dp, bot
from bot.handlers import start_handler, send_advert, ask_handler


def setup_routers(dp):
    dp.include_router(start_handler.router)
    dp.include_router(send_advert.router)
    dp.include_router(ask_handler.router)


async def main():
    setup_routers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
