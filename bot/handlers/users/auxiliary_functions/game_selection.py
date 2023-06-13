from bot.keyboards.inline.msg_pdf_html import inline_msg_html
from write_in_database import GamesData


async def process_game_selection(call, state, bot):
    await bot.answer_callback_query(call.id)  # Отправляем ответное уведомление пользователю, что его выбор обработан
    data = await state.get_data()  # Получаем сохраненные данные из состояния
    msg_id = data.get('msg_id')  # Получаем сохраненный ID сообщения
    if msg_id:
        await bot.delete_message(call.message.chat.id, msg_id)  # Удаляем сообщение по сохраненному ID

    game = GamesData.select().where(GamesData.id == call.data).get()  # Извлекаем выбранную игру из базы данных

    await call.message.answer(f"Ваш выбор игры: {game.Name}")  # Отправляем сообщение с выбранной игрой пользователю
    # Отправляем сообщение с встроенной клавиатурой для выбора формата представления
    msg_inline_msg_html = await call.message.answer("Выберите в каком виде представить",
                                                    reply_markup=inline_msg_html())
    # Сохраняем ID сообщения в состоянии
    await state.update_data(msg_inline_msg_html_id=msg_inline_msg_html.message_id)
    await state.update_data(selected_game=game)  # Сохраняем выбранную игру в состоянии
