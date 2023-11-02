from aiogram import Router, types, F
from button import get_GM_types, get_GM_chevrolet_types, get_GM_GMC_types, get_GM_cadillac_types


router_2 = Router()


@router_2.message(F.text == "GM")
async def open_GM(message: types.Message):
    await message.answer("🤗Welcome to GM", reply_markup = get_GM_types())


@router_2.message(F.text == "GMC")
async def open_gmc(message: types.Message):
    await message.answer("😲 The inside of GMC", reply_markup = get_GM_GMC_types())


@router_2.message(F.text == "Cadillac")
async def open_cyber_truck(message: types.Message):
    await message.answer("😲 The inside of Cadillac", reply_markup = get_GM_cadillac_types())


@router_2.message(F.text == "Chevrolet")
async def open_chevrolet(message: types.Message):
    await message.answer("😲 The inside of Chevrolet", reply_markup = get_GM_chevrolet_types())



