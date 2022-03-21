from aiogram import types

from common.bot_text.start import first_question, start_message, first_response
from common.bot_text.util_text import wrong_answer
from keyboards.default.keyboards import (
    yes_or_no_keyboard,
    next_keyboard,
)
from loader import dp
from states.main_states import AppStates
from common.user_answers import (
    YES,
    NO,
)
from utils.db_api.views.users import create_new_user


@dp.message_handler(commands=["start"], state="*")
async def bot_start(message: types.Message):
    create_new_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
    # await message.answer(start_message(message.from_user.full_name))
    await message.answer(first_question(), reply_markup=yes_or_no_keyboard)
    await AppStates.start_question_response.set()


@dp.message_handler(state='AppStates:start_question_response')
async def start_question_response(message: types.Message):
    if message.text not in [YES, NO]:
        await message.answer(wrong_answer())
        return
    await message.answer(first_response(message.text))
    await message.answer('Нажми "Дальше" чтобы продолжить.', reply_markup=next_keyboard)
    await AppStates.next()
