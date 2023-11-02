from aiogram import Router, types, F
from button import let_them_choose


router_4 = Router()


# Cadillac

@router_4.message(F.text == "Ats")
async def open_cadillac_ats(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/GPNSsBC", caption = "🚘 Name: Cadillac Ats\n\n💵 Price: $45000\n🌈 Color: Black\n🛠️ Auto: Automatic\n🕛 Year: 2018\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router_4.message(F.text == "Xts")
async def open_cadillac_xts(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/q1G0DQW", caption = "🚘 Name: Cadillac Xts\n\n💵 Price: $88000\n🌈 Color: Blue\n🛠️ Auto: Automatic\n🕛 Year: 2022\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router_4.message(F.text == "Escalade")
async def open_cadillac_escalade(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/LzM3tnv", caption = "🚘 Name: Cadillac Escalade\n\n💵 Price: $150000\n🌈 Color: White\n🛠️ Auto: Automatic\n🕛 Year: 2023\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())

