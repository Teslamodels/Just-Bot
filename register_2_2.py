from aiogram import Router, types, F
from button import let_them_choose


router_3 = Router()


# GMC

@router_3.message(F.text == "GMC Yukon XL")
async def open_gmc_yukon(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/2vJj03P", caption = "🚘 Name: GMC Yukon XL\n\n💵 Price: $110000\n🌈 Color: White\n🛠️ Auto: Automatic\n🕛 Year: 2019\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router_3.message(F.text == "GMC Sierra 1500")
async def open_gmc_sierra_1500(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/NZSvqkt", caption = "🚘 Name: GMC Sierra 1500\n\n💵 Price: $90000\n🌈 Color: Red\n🛠️ Auto: Automatic\n🕛 Year: 2022\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router_3.message(F.text == "GMC Sierra 2500HD")
async def open_gmc_sierra_2500(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/XyXwc2S", caption = "🚘 Name: GMC Sierra 2500HD\n\n💵 Price: $400000\n🌈 Color: Black\n🛠️ Auto: Automatic\n🕛 Year: 2023\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


















