from aiogram import types

from common.bot_text.age_test import third_question
from common.bot_text.choice import fourth_question
from common.bot_text.description import (
    second_response_question,
    second_question,
    second_response,
    detail_card,
)
from common.bot_text.util_text import wrong_answer
from keyboards.default.keyboards import (
    yes_or_no_keyboard,
    detail_description_keyboard,
    detail_description_keyboard_or_next,
    age_keyboard, choice_important_keyboard,
)
from loader import dp
from states.main_states import AppStates
from common.user_answers import (
    YES,
    NO,
    NEXT,
    DETAIL_ONE,
    DETAIL_TWO,
    DETAIL_THREE,
    DETAIL_FOUR,
)
from utils.db_api.views.girl_posts import get_girl_post
from utils.db_api.views.user_post_rel import is_posts_available


@dp.message_handler(state='AppStates:knowing_question')
async def knowing_question(message: types.Message):
    await message.answer(second_question(), reply_markup=yes_or_no_keyboard)
    await AppStates.next()


@dp.message_handler(state='AppStates:knowing_question_response')
async def knowing_question_response(message: types.Message):
    if message.text not in [YES, NO]:
        await message.answer(wrong_answer())
        return
    await message.answer(second_response(message.text))
    await message.answer(second_response_question(), reply_markup=detail_description_keyboard)
    await AppStates.next()


@dp.message_handler(state='AppStates:detail_description')
async def detail_description(message: types.Message):
    if message.text not in [DETAIL_ONE, DETAIL_TWO, DETAIL_THREE, DETAIL_FOUR]:
        await message.answer(wrong_answer())
        return

    await message.answer_photo(
        photo=detail_card(message.text)['photo_url'],
        caption=detail_card(message.text)['text'],
        reply_markup=detail_description_keyboard_or_next
    )
    await AppStates.next()


@dp.message_handler(state='AppStates:detail_description_or_next')
async def detail_description_or_next(message: types.Message, state: AppStates):
    if message.text not in [DETAIL_ONE, DETAIL_TWO, DETAIL_THREE, DETAIL_FOUR, NEXT]:
        await message.answer(wrong_answer())
        return

    if message.text in [DETAIL_ONE, DETAIL_TWO, DETAIL_THREE, DETAIL_FOUR]:
        await message.answer_photo(
            photo=detail_card(message.text)['photo_url'],
            caption=detail_card(message.text)['text'],
        )
    else:

        if is_posts_available(message.from_user.id):
            post = get_girl_post(message.from_user.id)

            async with state.proxy() as data:
                data['text'] = post['text']

            await message.answer(third_question())
            await message.answer_photo(
                photo=post['photo_url'],
                reply_markup=age_keyboard,
                caption='Угадайте, сколько ей лет?',
            )
            await AppStates.age_test_response.set()
        else:
            await message.answer(fourth_question(), reply_markup=choice_important_keyboard)
            await AppStates.choice_important_response.set()
