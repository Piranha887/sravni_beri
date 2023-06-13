# Импорт необходимых модулей и классов
from aiogram import types  # Импорт классов types из модуля aiogram
from aiogram.dispatcher import FSMContext  # Импорт класса FSMContext из модуля aiogram.dispatcher
from aiogram.types import CallbackQuery  # Импорт класса CallbackQuery из модуля aiogram.types

from bot.filters.check_type_letter import \
    LetterTypeCheck  # Импорт класса LetterTypeCheck из модуля bot.filters.check_type_letter
from bot.filters.check_type_nogoback import \
    NoGoBackCheck  # Импорт класса NoGoBackCheck из модуля bot.filters.check_type_nogoback
from bot.handlers.users.auxiliary_functions.game_selection import \
    process_game_selection  # Импорт функции process_game_selection из модуля bot.handlers.users.auxiliary_functions.game_selection
from bot.shows.show_information import \
    show_game_information  # Импорт функции show_game_information из модуля bot.shows.show_information
from bot.keyboards.default import keyboard_library  # Импорт функции keyboard_library из модуля bot.keyboards.default
from bot.keyboards.default.keyboard_main import \
    keyboard_main_menu  # Импорт функции keyboard_main_menu из модуля bot.keyboards.default.keyboard_main
from bot.keyboards.inline.letter_games import \
    inline_keyboard_letters  # Импорт функции inline_keyboard_letters из модуля bot.keyboards.inline.letter_games
from bot.loader import dp, bot  # Импорт объектов dp, bot из модуля bot.loader
from bot.states import SwitchMenu  # Импорт класса SwitchMenu из модуля bot.states
from bot.utils.misc import rate_limit  # Импорт функции rate_limit из модуля bot.utils.misc


# Декоратор для ограничения частоты вызова обработчика сообщений
@rate_limit(limit=3)
@dp.message_handler(LetterTypeCheck(), state=SwitchMenu.Library)
async def show_letter_games(message: types.Message, state: FSMContext):
    # Отправка ответного сообщения с выбранной буквой
    await message.answer("Ваш выбор буквы: " + message.text)
    # Отправка сообщения с выбором игры и кнопками для буквы
    msg = await message.answer('Выберите игру из меню', reply_markup=inline_keyboard_letters(message.text))
    # Отправка сообщения с инструкцией пользователю и кнопкой "Главное меню"
    await message.answer('Вы можете вернуться обратно с помощью команды "\U0001f519 Главное меню"',
                         reply_markup=keyboard_main_menu())
    await state.update_data(msg_id=msg.message_id)  # Сохранение ID сообщения в состоянии
    await SwitchMenu.Library_after_inline.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(NoGoBackCheck(), state=SwitchMenu.Library_after_inline)
async def letter_answer(call: CallbackQuery, state: FSMContext):
    # Обработка выбора игры по callback-запросу
    await process_game_selection(call, state, bot)
    await SwitchMenu.Library_shows.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(text='Сообщение', state=SwitchMenu.Library_shows)
async def show_game_msg(call: CallbackQuery, state: FSMContext):
    # Отображение информации об игре типа "Сообщение"
    await show_game_information(call, state, "Сообщение")
    await SwitchMenu.Library.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(text='PDF', state=SwitchMenu.Library_shows)
async def show_game_pdf(call: CallbackQuery, state: FSMContext):
    # Отображение информации об игре типа "PDF"
    await show_game_information(call, state, "PDF")
    await SwitchMenu.Library.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(text='HTML', state=SwitchMenu.Library_shows)
async def show_game_html(call: CallbackQuery, state: FSMContext):
    # Отображение информации об игре типа "HTML"
    await show_game_information(call, state, "HTML")
    await SwitchMenu.Library.set()


# Декоратор для ограничения частоты вызова обработчика callback-запросов
@rate_limit(limit=3)
@dp.callback_query_handler(text="Назад", state=SwitchMenu.Library_shows)
async def show_back_to_library_menu(call: CallbackQuery, state: FSMContext):
    # Обработка callback-запроса для возврата к меню выбора буквы
    data = await state.get_data()
    msg_inline_msg_html_id = data.get('msg_inline_msg_html_id')
    await bot.delete_message(call.message.chat.id, msg_inline_msg_html_id)
    await SwitchMenu.Library.set()
    await call.message.answer("Выберите букву из меню",
                              reply_markup=keyboard_library())  # Отправка сообщения с инструкцией пользователю
