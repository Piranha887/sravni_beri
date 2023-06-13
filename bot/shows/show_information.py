import base64
import io
import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from bot.shows.show_game import show_game
from bot.shows.show_html import show_html
from bot.shows.show_pdf import show_pdf
from bot.loader import bot


async def show_game_information(call: CallbackQuery, state: FSMContext, information_type: str):
    data = await state.get_data()
    msg_inline_msg_html_id = data.get('msg_inline_msg_html_id')  # Получаем идентификатор сообщения inline-кнопок HTML
    selected_game = data.get('selected_game')  # Получаем выбранную игру из состояния
    await call.message.answer(
        f"Ваш выбор представления информации: {information_type}")  # Отправляем сообщение с выбранным типом информации
    if msg_inline_msg_html_id:
        await bot.delete_message(call.message.chat.id,
                                 msg_inline_msg_html_id)  # Удаляем сообщение с inline-кнопками HTML
    if information_type == "Сообщение":
        media = types.MediaGroup()  # Создаем медиагруппу для отправки фотографий
        if selected_game.Image_HG:
            try:
                media.attach_photo(selected_game.Image_HG)  # Прикрепляем фотографию Image_HG к медиагруппе
            except:
                pass
        if selected_game.Image_gaga:
            try:
                media.attach_photo(selected_game.Image_gaga)  # Прикрепляем фотографию Image_gaga к медиагруппе
            except:
                pass
        if selected_game.Image_lavka:
            try:
                media.attach_photo(selected_game.Image_lavka)  # Прикрепляем фотографию Image_lavka к медиагруппе
            except:
                pass
        await call.message.answer(show_game(selected_game))  # Отправляем информацию о выбранной игре
        if media.media:
            await call.message.answer_media_group(media=media)  # Отправляем медиагруппу фотографий, если они есть
    elif information_type == "PDF":
        with io.BytesIO() as file_buffer:
            pdf_bytes = show_pdf(selected_game)  # Получаем байты PDF для выбранной игры
            base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')  # Кодируем байты PDF в base64
            document_data = base64.b64decode(base64_pdf)  # Декодируем base64 в байты
            file_buffer.write(document_data)
            file_buffer.seek(0)
            document = types.InputFile(file_buffer, filename=f"{selected_game.Name}.pdf")  # Создаем входной файл PDF
            await call.message.answer_document(document)  # Отправляем документ PDF
    elif information_type == "HTML":
        show_html(selected_game)  # Создаем HTML-файл для выбранной игры
        await call.message.answer_document(open(f"{selected_game.Name}.html", 'rb'))  # Отправляем HTML-файл
        os.remove(f"{selected_game.Name}.html")  # Удаляем временный HTML-файл
    await call.message.answer("Выберите кнопку из меню")  # Отправляем сообщение с инструкцией пользователю
