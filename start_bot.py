from aiogram import Dispatcher, types, Bot
from aiogram.enums.parse_mode import ParseMode
from Core.handlers import basic,csmoney
from Core.keyboards import menu
from os import getenv

import logging
import time
import asyncio


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="\033[34m {}".format('%(asctime)s - [%(levelname)s] - %(name)s'
                                                    '(%(filename)s.%(funcName)s(%(lineno)d) - %(message)s'))
    bot = Bot(token=getenv('TOCKEN'), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        basic.router,
        # csmoney.router
    )

    try:
        print("try...")
        await dp.start_polling(bot)
    finally:
        print("check finally")
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
