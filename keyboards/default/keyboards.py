from aiogram.types import ReplyKeyboardMarkup
from common.user_answers import (
    YES,
    NO,
    NEXT,
    DETAIL_ONE,
    DETAIL_TWO,
    DETAIL_THREE,
    DETAIL_FOUR,
    AGE_ONE,
    AGE_TWO,
    AGE_THREE,
    AGE_FOUR,
    AGE_MORE,
    CHOICE_IMPORTANT_ONE,
    CHOICE_IMPORTANT_TWO,
    CHOICE_IMPORTANT_THREE,
    CHOICE_IMPORTANT_FOUR,
    BRAND_ONE,
    BRAND_TWO,
    BRAND_THREE,
    BRAND_FOUR,
    BRAND_FIVE,
    BRAND_SIX,
)


yes_or_no_keyboard = ReplyKeyboardMarkup(
    keyboard=[[YES, NO]],
    resize_keyboard=True
)

next_keyboard = ReplyKeyboardMarkup(
    keyboard=[[NEXT]],
    resize_keyboard=True
)

detail_description_keyboard = ReplyKeyboardMarkup(
    keyboard=[[DETAIL_ONE, DETAIL_TWO], [DETAIL_THREE]],
    resize_keyboard=True
)

detail_description_keyboard_or_next = ReplyKeyboardMarkup(
    keyboard=[[DETAIL_ONE, DETAIL_TWO], [DETAIL_THREE], [NEXT]],
    resize_keyboard=True
)

age_keyboard = ReplyKeyboardMarkup(
    keyboard=[[AGE_ONE, AGE_TWO], [AGE_THREE, AGE_FOUR]],
    resize_keyboard=True
)

age_again_keyboard = ReplyKeyboardMarkup(
    keyboard=[[AGE_MORE, NEXT]],
    resize_keyboard=True
)

choice_important_keyboard = ReplyKeyboardMarkup(
    keyboard=[[CHOICE_IMPORTANT_ONE, CHOICE_IMPORTANT_TWO], [CHOICE_IMPORTANT_THREE]],
    resize_keyboard=True
)

choice_important_keyboard_or_next = ReplyKeyboardMarkup(
    keyboard=[[CHOICE_IMPORTANT_ONE, CHOICE_IMPORTANT_TWO], [CHOICE_IMPORTANT_THREE], [NEXT]],
    resize_keyboard=True
)

brand_keyboard = ReplyKeyboardMarkup(
    keyboard=[[BRAND_ONE, BRAND_THREE], [BRAND_FOUR, BRAND_FIVE], [BRAND_SIX]],
    resize_keyboard=True
)
