from aiogram import Router, types, F


router_8 = Router()


@router_8.callback_query(F.data == "Not Buy")
async def we_will_make_it_better(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("You can see other one but we will fix it ⚙️")


@router_8.callback_query(F.data == "Buy")
async def good_decision(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🛒 The product is successfully added to basket 👍")


