from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, KeyboardButton

clear_keyboard = ReplyKeyboardRemove()
mainmenu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Parser"), KeyboardButton(text="D&D")],
    [KeyboardButton(text="Button1"), KeyboardButton(text="Button2")]],
    resize_keyboard=True,
)
parsermenu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="csmoney"), KeyboardButton(text="csmarket")],
    [KeyboardButton(text="Назад"), KeyboardButton(text="В главное меню")]],
    resize_keyboard=True,
)
csmoney_keyboard = ReplyKeyboardMarkup(keyboard=
                                       [[KeyboardButton(text="🔪Ножи"), KeyboardButton(text="🥊Перчатки")],
                                        [KeyboardButton(text="🔫Снаперские винтовки")],
                                        [KeyboardButton(text="Назад"), KeyboardButton(text="В главное меню")]],
                                       resize_keyboard=True)
