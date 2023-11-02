from aiogram import Router, types, F
from button import let_them_choose


router_5 = Router()


# Chevrolet

@router_5.message(F.text == "Chevrolet Tahoe")
async def open_chevrolet_tahoe(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/WndJwVd", caption = "🚘 Name: Chevrolet Tahoe\n\n💵 Price: $350000\n🌈 Color: Red\n🛠️ Auto: Automatic\n🕛 Year: 2023\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router_5.message(F.text == "Chevrolet Camaro")
async def open_chevrolet_camaro(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/V25L8qj", caption = "🚘 Name: Chevrolet Camaro\n\n💵 Price: $77115\n🌈 Color: Yellow\n🛠️ Auto: Automatic\n🕛 Year: 2022\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router_5.message(F.text == "Chevrolet Corvette")
async def open_chevrolet_corvette(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/6s5DJZ0", caption = "🚘 Name: Chevrolet Corvette\n\n💵 Price: $65000\n🌈 Color: Orange\n🛠️ Auto: Machenic\n🕛 Year: 2020\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())
