from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from states.admin_states import AdminStates
from utils.db_api.views.girl_posts import create_girl_post


@dp.message_handler(commands=["upload"], state="*", is_admin=True)
async def upload(message: types.Message):
    await message.answer('Загрузка поста девушки к вопросу о возрасте', reply_markup=ReplyKeyboardRemove())
    await message.answer('Загрузите фото девушки:', reply_markup=ReplyKeyboardRemove())
    await AdminStates.photo.set()


@dp.message_handler(content_types=['photo'], state="AdminStates:photo", is_admin=True)
async def photo(message: types.Message, state: AdminStates):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await AdminStates.next()
    await message.answer('Теперь введите описание:')


@dp.message_handler(state="AdminStates:text", is_admin=True)
async def text(message: types.Message, state: AdminStates):
    async with state.proxy() as data:
        data['text'] = message.text
    create_girl_post(data['photo'], data['text'])
    await state.finish()
    await message.answer('Пост загпружен в БД!')