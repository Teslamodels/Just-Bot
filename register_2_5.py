from aiogram import Router, types, F
from button import get_GM_types


router_6 = Router()


@router_6.message(F.text == "🔁 Return to Chevrolet models")
async def back_to_GM_model_1(message: types.Message):
    await message.answer("Have a good selection", reply_markup = get_GM_types())


@router_6.message(F.text == "🔁 Return to GMC models")
async def back_to_GM_model_2(message: types.Message):
    await message.answer("Have a good selection", reply_markup = get_GM_types())


@router_6.message(F.text == "🔁 Return to Cadillac models")
async def back_to_GM_model_3(message: types.Message):
    await message.answer("Have a good selection", reply_markup = get_GM_types())

