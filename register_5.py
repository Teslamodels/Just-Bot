from aiogram import Router, types, F
from button import get_car_types


router_9 = Router()


@router_9.message(F.text == "↩️ Back")
async def back(message: types.Message):
    await message.answer("📄 Please, choose the page", reply_markup = get_car_types())

