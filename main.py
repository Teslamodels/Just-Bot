import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from config import bot_token
from button import get_car_types

from register_1 import router
from register_2_1 import router_2
from register_2_2 import router_3
from register_2_3 import router_4 
from register_2_4 import router_5
from register_2_5 import router_6
from register_3 import router_7
from register_4 import router_8
from register_5 import router_9

bot = Bot(token = bot_token, parse_mode = ParseMode.MARKDOWN_V2)

dp = Dispatcher()


@dp.message(CommandStart())
async def let_it_start(message: types.Message):
    await message.answer(f"👋 Hi {message.from_user.full_name}\n\nWelcome to the world of cars of 21s century 🤗", reply_markup = get_car_types())





async def main():
    dp.include_routers(router, router_2, router_3, router_4, router_5, router_6, router_7, router_8, router_9)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level = logging.INFO, stream = sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Error")