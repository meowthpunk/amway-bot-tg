from aiogram import types

from common.bot_text.choice import fourth_response, give_sticker
from common.bot_text.util_text import wrong_answer, STICKER_ID
from keyboards.default.keyboards import (
    next_keyboard,
    choice_important_keyboard_or_next,
)
from loader import dp
from states.main_states import AppStates
from common.user_answers import (
    CHOICE_IMPORTANT_ONE,
    CHOICE_IMPORTANT_TWO,
    CHOICE_IMPORTANT_THREE,
    CHOICE_IMPORTANT_FOUR, NEXT,
)


@dp.message_handler(state='AppStates:choice_important_response')
async def choice_important_question(message: types.Message):
    if message.text not in [
        CHOICE_IMPORTANT_ONE,
        CHOICE_IMPORTANT_TWO,
        CHOICE_IMPORTANT_THREE,
        CHOICE_IMPORTANT_FOUR,
    ]:
        await message.answer(wrong_answer())
        return

    await message.answer(fourth_response(message.text), reply_markup=choice_important_keyboard_or_next)
    await AppStates.next()


@dp.message_handler(state='AppStates:choice_important_response_or_next')
async def choice_important_question_or_next(message: types.Message):
    if message.text not in [
        CHOICE_IMPORTANT_ONE,
        CHOICE_IMPORTANT_TWO,
        CHOICE_IMPORTANT_THREE,
        CHOICE_IMPORTANT_FOUR,
        NEXT,
    ]:
        await message.answer(wrong_answer())
        return
    if message.text in [
        CHOICE_IMPORTANT_ONE,
        CHOICE_IMPORTANT_TWO,
        CHOICE_IMPORTANT_THREE,
        CHOICE_IMPORTANT_FOUR,
    ]:
        await message.answer(fourth_response(message.text), reply_markup=choice_important_keyboard_or_next)
    else:
        await message.answer(give_sticker())
        await message.answer_sticker(STICKER_ID, reply_markup=next_keyboard)
        await AppStates.next()
