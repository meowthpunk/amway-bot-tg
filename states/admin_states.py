from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminStates(StatesGroup):
    photo = State()
    text = State()
