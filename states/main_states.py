from aiogram.dispatcher.filters.state import StatesGroup, State


class AppStates(StatesGroup):
    start_question_response = State()
    knowing_question = State()
    knowing_question_response = State()
    detail_description = State()
    detail_description_or_next = State()
    age_test_response = State()
    age_test_question = State()
    choice_important_response = State()
    choice_important_response_or_next = State()
    final_question = State()
    final_response = State()
