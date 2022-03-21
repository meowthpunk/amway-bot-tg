from common.user_answers import (
    YES,
    NO,
)


def start_message(username):
    return f'Привет {username}!🙂 Я чат бот Artistry.\n\n' \
           'Потрать 5 минут на диалог со мной, чтобы получить персональную рекомендацию по уходу за кожей лица.\n' \
           'К тому же ты получишь скидку при регистрации 15%'


def first_question():
    return 'Ну что, начнем? 😉'


def first_response(user_answer):
    if user_answer == YES:
        text = 'Отлично, я очень рад! 😎'
    elif user_answer == NO:
        text = 'Ну может быть в другой раз 😔?'
    else:
        text = 'Введите "Да" или "Нет".'
    return text
