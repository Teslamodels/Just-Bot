from aiogram import Router, types, F
from button import let_them_choose, get_ford_types


router_7 = Router()


# Ford

@router_7.message(F.text == "Ford")
async def open_tesla(message: types.Message):
    await message.answer("Have a good option", reply_markup = get_ford_types())


@router_7.message(F.text == "Ford F-150")
async def open_ford_F_150(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/m0rFnwF", caption = "🚘 Name: Ford F 150\n\n💵 Price: $55000\n🌈 Color: Red\n🛠️ Auto: Automatic\n🕛 Year: 20219\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router_7.message(F.text == "Ford Mustang")
async def open_ford_Mustang(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/cFJMtWs", caption = "🚘 Name: Ford Mustang\n\n💵 Price: $35000\n🌈 Color: Orange\n🛠️ Auto: Machenic\n🕛 Year: 2019\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router_7.message(F.text == "Ford Fusion")
async def open_ford_(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/9rJgTqR", caption = "🚘 Name: Ford Fusion\n\n💵 Price: $28000\n🌈 Color: White\n🛠️ Auto: Automatic\n🕛 Year: 20219\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


