from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

from common.bot_text.choice import fourth_question
from common.bot_text.util_text import wrong_answer
from keyboards.default.keyboards import (
    age_keyboard,
    age_again_keyboard,
    choice_important_keyboard,
)
from loader import dp
from states.main_states import AppStates
from common.user_answers import (
    NEXT,
    AGE_ONE,
    AGE_TWO,
    AGE_THREE,
    AGE_FOUR,
    AGE_MORE,
)
from utils.db_api.views.girl_posts import get_girl_post
from utils.db_api.views.user_post_rel import is_posts_available, delete_relationships


@dp.message_handler(state='AppStates:age_test_response')
async def age_test_response(message: types.Message, state: AppStates):
    if message.text not in [AGE_ONE, AGE_TWO, AGE_THREE, AGE_FOUR]:
        await message.answer(wrong_answer())
        return

    async with state.proxy() as data:
        data['q'] = message.text

    if is_posts_available(message.from_user.id):
        await message.answer(data['text'], reply_markup=age_again_keyboard)
    else:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(NEXT)
        await message.answer(data['text'], reply_markup=keyboard)
    await AppStates.age_test_question.set()


@dp.message_handler(state='AppStates:age_test_question')
async def age_test_question(message: types.Message, state: AppStates):
    if message.text not in [NEXT, AGE_MORE]:
        await message.answer(wrong_answer())
        return

    if message.text == AGE_MORE:
        post = get_girl_post(message.from_user.id)

        async with state.proxy() as data:
            data['text'] = post['text']

        await message.answer_photo(
            photo=post['photo_url'],
            reply_markup=age_keyboard,
            caption='Угадайте, сколько ей лет?',
        )
        await AppStates.age_test_response.set()
    else:
        delete_relationships(message.from_user.id)
        await message.answer(fourth_question(), reply_markup=choice_important_keyboard)
        await AppStates.choice_important_response.set()
