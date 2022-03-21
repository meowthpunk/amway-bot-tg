from aiogram import types
from aiogram.dispatcher import FSMContext


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
async def bot_echo(message: types.Message):
    await message.answer(f"Введите команду /start")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
