from aiogram import Bot, types, Router
from aiogram.filters import Command
from Core.keyboards import menu
from Core.others.models import MenuStates
from aiogram import F

router = Router()

@router.message(F.text == "csmoney")
async def csmoney_menu_buttons(message: types.Message):
    await message.answer("Csmoney меню", reply_markup=menu.csmoney_keyboard)


# def register_handlers_csmoney(dp: Dispatcher):
#     dp.message.register(csmoney_menu_buttons, F.text == "csmoney")
