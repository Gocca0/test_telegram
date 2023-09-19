from aiogram.fsm.state import State, StatesGroup


class MenuStates(StatesGroup):
    MAIN_MENU = State()
    PARSING = State()
    CSMONEY = State()
