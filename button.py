from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



cars = ["Tesla", "GM", "Ford"]

def get_car_types():
    builder = ReplyKeyboardBuilder()
    for car in cars:
        builder.add(KeyboardButton(text = car))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard = True)



Tesla = ["Tesla Model S", "Tesla Model E", "Tesla Model X", "Tesla Model 3", "Tesla Roadster", "Tesla Cyber Truck", "Tesla Semi", "Tesla Model Y"]

def get_tesla_types():
    builder_2 = ReplyKeyboardBuilder()
    for elon in Tesla:
        builder_2.add(KeyboardButton(text = elon))
    builder_2.add(KeyboardButton(text = "↩️ Back"))
    builder_2.adjust(2)
    return builder_2.as_markup(resize_keyboard = True)



GM = ["Chevrolet", "GMC", "Cadillac"]

def get_GM_types():
    builder_3 = ReplyKeyboardBuilder()
    for gm in GM:
        builder_3.add(KeyboardButton(text = gm))
    builder_3.add(KeyboardButton(text = "↩️ Back"))
    builder_3.adjust(1)
    return builder_3.as_markup(resize_keyboard = True)



Chevrolet = ["Chevrolet Corvette", "Chevrolet Camaro", "Chevrolet Tahoe"]

def get_GM_chevrolet_types():
    builder_4 = ReplyKeyboardBuilder()
    for chevrolet in Chevrolet:
        builder_4.add(KeyboardButton(text = chevrolet))
    builder_4.add(KeyboardButton(text = "🔁 Return to Chevrolet models"))
    builder_4.add(KeyboardButton(text = "↩️ Back"))
    builder_4.adjust(1)
    return builder_4.as_markup(resize_keyboard = True)



GMC = ["GMC Sierra 2500HD", "GMC Sierra 1500", "GMC Yukon XL"]

def get_GM_GMC_types():
    builder_5 = ReplyKeyboardBuilder()
    for gmc in GMC:
        builder_5.add(KeyboardButton(text = gmc))
    builder_5.add(KeyboardButton(text = "🔁 Return to GMC models"))
    builder_5.add(KeyboardButton(text = "↩️ Back"))
    builder_5.adjust(1)
    return builder_5.as_markup(resize_keyboard = True)



Cadillac = ["Ats", "Escalade", "Xts"]

def get_GM_cadillac_types():
    builder_6 = ReplyKeyboardBuilder()
    for cadillac in Cadillac:
        builder_6.add(KeyboardButton(text = cadillac))
    builder_6.add(KeyboardButton(text = "🔁 Return to Cadillac models"))
    builder_6.add(KeyboardButton(text = "↩️ Back"))
    builder_6.adjust(1)
    return builder_6.as_markup(resize_keyboard = True)



Ford = ["Ford Mustang", "Ford F-150", "Ford Fusion"]

def get_ford_types():
    builder_7 = ReplyKeyboardBuilder()
    for fords in Ford:
        builder_7.add(KeyboardButton(text = fords))
    builder_7.add(KeyboardButton(text = "↩️ Back"))
    builder_7.adjust(1)
    return builder_7.as_markup(resize_keyboard = True)



def let_them_choose():
    builder_3 = InlineKeyboardBuilder()
    builder_3.add(InlineKeyboardButton(text = "✅ Buy", callback_data = "Buy"))
    builder_3.add(InlineKeyboardButton(text = "❌ Another type", callback_data = "Not Buy"))
    builder_3.adjust(2)
    return builder_3.as_markup()