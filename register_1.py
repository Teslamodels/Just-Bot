from aiogram import Router, types, F
from button import get_tesla_types, let_them_choose


router = Router()


@router.message(F.text == "Tesla")
async def open_tesla(message: types.Message):
    await message.answer("🫡 Tesla is waiting for you, dear user", reply_markup = get_tesla_types())


@router.message(F.text == "Tesla Semi")
async def open_model_semi(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/JkwxRkG", caption = "🚘 Name: Tesla Semi\n\n💵 Price: $900000\n🌈 Color: Gray\n🛠️ Auto: Electric\n🕛 Year: 2020\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router.message(F.text == "Tesla Model S")
async def open_model_s(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/P1YTXzN", caption = "🚘 Name: Tesla Model S\n\n💵 Price: $74990\n🌈 Color: Red\n🛠️ Auto: Electric\n🕛 Year: 2023\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router.message(F.text == "Tesla Model Y")
async def open_model_e(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/P52NL9Z", caption = "🚘 Name: Tesla Model Y\n\n💵 Price: $55000\n🌈 Color: Blue\n🛠️ Auto: Electric\n🕛 Year: 2020\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router.message(F.text == "Tesla Roadster")
async def open_roadster(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/TrV6Hcm", caption = "🚘 Name: Tesla Roadster\n\n💵 Price: $65000\n🌈 Color: Red\n🛠️ Auto: Electric\n🕛 Year: 2020\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router.message(F.text == "Tesla Model E")
async def open_model_y(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/PGqmZW8", caption = "🚘 Name: Tesla Model E\n\n💵 Price: $56380\n🌈 Color: Black\n🛠️ Auto: Electric\n🕛 Year: 2020\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router.message(F.text == "Tesla Model 3")
async def open_model_3(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/vZdMQxp", caption = "🚘 Name: Tesla Model 3\n\n💵 Price: $65021\n🌈 Color: White\n🛠️ Auto: Electric\n🕛 Year: 2022\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router.message(F.text == "Tesla Model X")
async def open_model_x(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/NymRbpW", caption = "🚘 Name: Tesla Model X\n\n💵 Price: $111554\n🌈 Color: White\n🛠️ Auto: Electric\n🕛 Year: 2021\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())


@router.message(F.text == "Tesla Cyber Truck")
async def open_cyber_truck(message: types.Message):
    await message.answer_photo(photo = "https://ibb.co/MC0ZkpB/", caption = "🚘 Name: Tesla Cyber Truck\n\n💵 Price: $350000\n🌈 Color: Gray\n🛠️ Auto: Electric\n🕛 Year: 2019\n\n\n🤔Just make the right decision", reply_markup = let_them_choose())

