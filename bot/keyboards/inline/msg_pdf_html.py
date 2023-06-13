# Импорт необходимых модулей и классов
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Функция для создания inline клавиатуры с HTML-кнопками
def inline_msg_html():
    markup = InlineKeyboardMarkup(row_width=3)  # Создание объекта клавиатуры с шириной строки 3

    # Создание кнопки для отправки сообщения
    message_button = InlineKeyboardButton('Сообщение', callback_data='Сообщение')

    # Создание кнопки для отправки PDF-файла
    pdf_button = InlineKeyboardButton('PDF', callback_data='PDF')

    # Создание кнопки для отправки HTML-страницы
    html_button = InlineKeyboardButton('HTML', callback_data='HTML')

    # Создание кнопки для возврата назад
    back_button = InlineKeyboardButton('Назад', callback_data='Назад')

    # Добавление кнопок в клавиатуру
    markup.add(message_button, pdf_button, html_button)
    markup.add(back_button)

    return markup  # Возврат созданной клавиатуры

