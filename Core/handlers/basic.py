from aiogram import Bot, types, Dispatcher, Router, F
from aiogram.filters import Command, CommandStart
from Core.keyboards import menu
from Core.handlers import csmoney
from Core.others.models import MenuStates

router = Router()
# async def get_start(message: types.Message, bot: Bot):
#     await bot.send_message(message.from_user.id,
#                            f"id user = {message.from_user.id}")
#     print(message.from_user.id)

# Command(commands=['start', 'menu'])
# @router.startup()
# async def start_bot(bot: Bot):
#     await bot.send_message(399063250, text='Бот запущен')
#     print("\33[32m{}".format('Бот запущен'))
#
#
# @router.shutdown()
# async def stop_bot(bot: Bot):
#     await bot.send_message(399063250, text='Бот остановлен')
#     print("\33[32m{}".format('Бот остановлен'))

@router.message(F.text == "/start")
async def start_button_menu(message: types.Message):
    # MenuStates.MAIN_MENU
    await message.answer("Главное меню", reply_markup=menu.mainmenu_keyboard)


@router.message(F.text == "В главное меню")
async def start_button_menu(message: types.Message):
    # MenuStates.MAIN_MENU
    await message.answer("Главное меню", reply_markup=menu.mainmenu_keyboard)


@router.message(F.text == "Parser")
async def parsing_menu_buttons(message: types.Message):
    await message.answer("Parsing menu", reply_markup=menu.parsermenu_keyboard)




# def register_handlers_basic(dp:Dispatcher):
#     # Start menu
#     dp.message.register(start_button_menu, ))
#     dp.message.register(start_button_menu, F.text == "В главное меню")
#     dp.message.register(parsing_menu_buttons, F.text == "Parser")
#     # CSMONEY menu
#     dp.message.register(csmoney.csmoney_menu_buttons, F.text == "csmoney")
#     # dp.message.register(get_start)