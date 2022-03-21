from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from common.bot_text.final import fifth_response, fifth_question
from common.bot_text.util_text import wrong_answer
from keyboards.default.keyboards import (
    brand_keyboard,
)
from loader import dp
from states.main_states import AppStates
from common.user_answers import (
    NEXT,
    BRAND_ONE,
    BRAND_TWO,
    BRAND_THREE,
    BRAND_FOUR,
    BRAND_FIVE,
    BRAND_SIX,
)


@dp.message_handler(state='AppStates:final_question')
async def final_question(message: types.Message):
    if message.text not in [NEXT]:
        await message.answer(wrong_answer())
        return

    await message.answer(fifth_question(), reply_markup=brand_keyboard)
    await AppStates.next()


@dp.message_handler(state='AppStates:final_response')
async def final_response(message: types.Message):
    if message.text not in [
        BRAND_ONE,
        BRAND_TWO,
        BRAND_THREE,
        BRAND_FOUR,
        BRAND_FIVE,
        BRAND_SIX,
    ]:
        await message.answer(wrong_answer())
        return

    await message.answer(
        fifth_response(message.text)['text'],
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=types.ParseMode.HTML
    )
    await message.answer_video(
        fifth_response(message.text)['video_url']
    )

    button = types.InlineKeyboardButton(
        text="Купить!",
        url=fifth_response(message.text)['shop_link']
    )
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(button)
    await message.answer(
        'Перейти к товару ⬇',
        reply_markup=keyboard,
        parse_mode=types.ParseMode.HTML
    )
