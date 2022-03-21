from common.user_answers import (
    CHOICE_IMPORTANT_ONE,
    CHOICE_IMPORTANT_TWO,
    CHOICE_IMPORTANT_THREE,
    CHOICE_IMPORTANT_FOUR,
)


def fourth_question():
    return 'Что для вас является важным при выборе косметических средств для себя?'


def fourth_response(user_answer):
    if user_answer == CHOICE_IMPORTANT_ONE:
        text = text = 'Мы используем только допустимые ингредиенты 🌿растительного происхождения. и наши средства не тестируютс на животных.\n⛔ В составе продукции Artistry вы не найдете такие опасные ингредиенты, как парабены, сульфаты, силиконы, фталаты и синтетические ароматизаторы - ☝️мы просто их не используем!'

    elif user_answer == CHOICE_IMPORTANT_TWO:
        text = '💁‍♀️ Выбирая косметику, мы часто полагаемся на рекламу.\n☝️Эффективность же нашей продукции  подтверждается потребительскими испытаниями. Информация о результатах исследования  есть на нашем сайте по каждому продукту.'
    elif user_answer == CHOICE_IMPORTANT_THREE:
        text = 'Artistry является единственным брендом премиум класса в индустрии прямых продаж 🚀\n🏆 Наш Увлажняющий крем-гель для век ARTISTRY SKIN NUTRITION™️ одержал заслуженную победу в премии Glamour Best of Beauty в категории «Лицо». '
    elif user_answer == CHOICE_IMPORTANT_FOUR:
        text = text = 'Выбирая косметику, мы часто полагаемся на рекламу. Эффективность же нашей продукции  подтверждается потребительскими испытаниями. Информация о результатах ислледования  есть на нашем сайте по каждому продукту.'
    else:
        text = 'Введите "Да" или "Нет".'
    return text


def give_sticker():
    return 'Спасибо, что интересуешься нашим брендом!\n' \
           'Лови небольшой <b>подарок</b> - набор наших стикеров.\n' \
           'Чтобы сохранить их себе, нажми <b>"Добавить стикеры"</b> в правом нижнем углу.'
