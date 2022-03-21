from aiogram import Dispatcher, types

from handlers.users.admin_handlers.upload_girl_post import upload, photo, text
from handlers.users.echo import bot_echo, bot_echo_all
from handlers.users.main_funnel.age_test import age_test_response, age_test_question
from handlers.users.main_funnel.choice_important import choice_important_question
from handlers.users.main_funnel.description import (
    knowing_question,
    knowing_question_response,
    detail_description,
    detail_description_or_next
)
from handlers.users.main_funnel.final import final_response, final_question
from handlers.users.main_funnel.start import bot_start, start_question_response


def register_handlers_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo, state=None)

    # ONLY FOR DEVELOPMENT
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)


def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands="start", state="*")
    dp.register_message_handler(start_question_response, state='AppStates:start_question_response')
    dp.register_message_handler(knowing_question, state='AppStates:knowing_question')
    dp.register_message_handler(knowing_question_response, state='AppStates:knowing_question_response')
    dp.register_message_handler(detail_description, state='AppStates:detail_description')
    dp.register_message_handler(detail_description_or_next, state='AppStates:detail_description_or_next')
    dp.register_message_handler(age_test_response, state='AppStates:age_test_response')
    dp.register_message_handler(age_test_question, state='AppStates:age_test_question')
    dp.register_message_handler(choice_important_question, state='AppStates:choice_important_response')
    dp.register_message_handler(final_question, state='AppStates:final_question')
    dp.register_message_handler(final_response, state='AppStates:final_response')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(upload, commands="upload", state="*", is_admin=True)
    dp.register_message_handler(photo, content_types=['photo'], state="AdminStates:photo", is_admin=True)
    dp.register_message_handler(text, state="AdminStates:text", is_admin=True)
