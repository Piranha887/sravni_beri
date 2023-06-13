import io
import textwrap

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def parse_string(input_string, delimiter, prefix):
    segments = input_string.split(delimiter)
    parsed_strings = [prefix + segment.strip() for segment in segments]
    return parsed_strings


def empty_check(data):
    if data != '':
        return True
    else:
        return False


def show_pdf(game):
    # Создание PDF-документа
    buffer = io.BytesIO()
    page_height = letter[1]
    c = canvas.Canvas(buffer, pagesize=(letter[0], page_height))
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    # Создание стилей для текста
    styles = getSampleStyleSheet()
    heading_style = styles['Title']
    heading_style.fontName = 'Arial'

    # Настройка шрифта и размера текста
    font_name = "Arial"
    font_size = 12

    # Запись параметров в PDF документ
    y = page_height - 50  # Начальная позиция по оси Y
    line_height = 18  # Высота строки
    max_lines_per_page = (page_height - y) // line_height

    c.setFont(heading_style.fontName, font_size + 10)
    c.drawCentredString(300, y, game.Name)
    y -= line_height

    if empty_check(game.Slogan):
        c.setFont(font_name, font_size - 1)
        c.drawCentredString(300, y, game.Slogan)
        y -= line_height

    if empty_check(game.Tags):
        y -= line_height
        c.setFont(font_name, font_size)
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, "Тэги: ")
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        c.drawString(85, y, game.Tags)
        y -= line_height

    if empty_check(game.Language):
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, "Язык: ")
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        c.drawString(85, y, game.Language)
        y -= line_height

    if empty_check(game.Player):
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, "Количество игроков: ")
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        c.drawString(170, y, game.Player)
        y -= line_height

    if empty_check(game.Time):
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, "Время игры: ")
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        c.drawString(125, y, game.Time + " мин.")
        y -= line_height

    if empty_check(game.Age):
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, "Возрастное ограничение: ")
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        c.drawString(190, y, game.Age)
        y -= line_height

    if empty_check(game.Rating_bgg):
        rating_bgg = "Рейтинг BGG:"
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, rating_bgg)
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        c.drawString(130, y, game.Rating_bgg)
        y -= line_height

    if empty_check(game.Rating_tesera):
        rating_tesera = "Рейтинг Tesera:"
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, rating_tesera)
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        c.drawString(140, y, game.Rating_tesera)
        y -= line_height

    price = f"{game.Price} ₽ [взята по ссылке HobbyGames]"
    c.setFillColor(colors.purple)  # Фиолетовый цвет
    c.drawString(50, y, "Цена:")
    c.setFillColor(colors.black)  # Возвращаем черный цвет
    c.drawString(85, y, price)
    y -= line_height
    y -= line_height

    if empty_check(game.Plus):
        plus = "Плюсы:"
        plus_params = parse_string(game.Plus, '^', '+')
        c.setFont(font_name, font_size)
        if y <= line_height:
            c.showPage()
            y = page_height - line_height
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, plus)
        y -= line_height
        c.setFillColor(colors.black)  # Черный цвет
        c.setFont(font_name, font_size)
        for param in plus_params:
            if y <= line_height:
                c.showPage()
                y = page_height - line_height
            wrapped_params = textwrap.wrap(param, width=70)
            for line in wrapped_params:
                c.drawString(50, y, line.rstrip('+'))
                y -= line_height

    if empty_check(game.Minus):
        minus = "Минусы:"
        minus_params = parse_string(game.Minus, '^', '-')
        c.setFont(font_name, font_size)
        if y <= line_height:
            c.showPage()
            y = page_height - line_height
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, minus)
        y -= line_height
        c.setFillColor(colors.black)  # Черный цвет
        c.setFont(font_name, font_size)
        for param in minus_params:
            if y <= line_height:
                c.showPage()
                y = page_height - line_height
            wrapped_params = textwrap.wrap(param, width=70)
            for line in wrapped_params:
                c.drawString(50, y, line.rstrip('-'))
                y -= line_height

    if empty_check(game.Feature):
        feature = "Особенности:"
        feature_params = parse_string(game.Feature, '^', '*')
        c.setFont(font_name, font_size)
        if y <= line_height:
            c.showPage()
            y = page_height - line_height
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, feature)
        y -= line_height
        c.setFillColor(colors.black)  # Черный цвет
        c.setFont(font_name, font_size)
        for param in feature_params:
            if y <= line_height:
                c.showPage()
                y = page_height - line_height
            wrapped_params = textwrap.wrap(param, width=70)
            for line in wrapped_params:
                c.drawString(50, y, line.rstrip('*'))
                y -= line_height

    if empty_check(game.Description):
        description = game.Description
        lines = textwrap.wrap(description, width=70)
        c.setFont(font_name, font_size)
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, "Описание:")
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        y -= line_height
        for line in lines:
            if y <= line_height:
                c.showPage()
                y = page_height - line_height
                c.setFont(font_name, font_size)
                # c.setFillColor(colors.purple)  # Фиолетовый цвет
            c.drawString(50, y, line)
            # c.setFillColor(colors.black)  # Возвращаем черный цвет
            y -= line_height

    if empty_check(game.Resume):
        resume = "Резюме:"
        c.setFont(font_name, font_size)
        if y <= line_height:
            c.showPage()
            y = page_height - line_height
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, resume)
        y -= line_height
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        resume_lines = textwrap.wrap(game.Resume, width=70)
        for line in resume_lines:
            c.drawString(85, y, line)
            y -= line_height
        # y = check_and_move_to_third_page(c, y, line_height, page_height, resume_lines, font_name, font_size)

    if empty_check(game.Equipment):
        c.setFont(font_name, font_size)
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, "Комплектация:")
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        y -= line_height
        c.setFont(font_name, font_size)
        if y <= line_height:
            c.setFont(font_name, font_size)
            c.showPage()
            y = page_height - line_height

        equipment_lines = game.Equipment.split(",")  # Разделение строк по запятой
        for line in equipment_lines:
            c.drawString(50, y, line.strip())  # Отрисовка каждой строки
            y -= line_height

    # y = check_and_move_to_third_page(c, y, line_height, page_height, equipment_lines, font_name, font_size)

    if y <= line_height:
        c.setFont(font_name, font_size)
        c.showPage()
        y = page_height - line_height

    c.setFont(font_name, font_size)
    c.setFillColor(colors.purple)  # Фиолетовый цвет
    c.drawString(50, y, "Ссылка на игру в HobbyGames: ")
    c.setFillColor(colors.blue)  # Фиолетовый цвет
    c.drawString(230, y, game.Url_game_hg)
    c.setFillColor(colors.black)  # Возвращаем черный цвет
    y -= line_height

    if y <= line_height:
        c.setFont(font_name, font_size)
        c.showPage()
        y = page_height - line_height

    c.setFont(font_name, font_size)
    c.setFillColor(colors.purple)  # Фиолетовый цвет
    c.drawString(50, y, "Ссылка на игру в GagaGames: ")
    c.setFillColor(colors.blue)  # Фиолетовый цвет
    c.drawString(230, y, game.Url_game_gaga)
    c.setFillColor(colors.black)  # Возвращаем черный цвет
    y -= line_height

    if y <= line_height:
        c.setFont(font_name, font_size)
        c.showPage()
        y = page_height - line_height

    c.setFont(font_name, font_size)
    c.setFillColor(colors.purple)  # Фиолетовый цвет
    c.drawString(50, y, "Ссылка на игру в LavkaIgr: ")
    c.setFillColor(colors.blue)  # Фиолетовый цвет
    c.drawString(230, y, game.Url_game_lavka)
    c.setFillColor(colors.black)  # Возвращаем черный цвет
    y -= line_height

    if empty_check(game.Rules):
        c.setFont(font_name, font_size)
        c.setFillColor(colors.purple)  # Фиолетовый цвет
        c.drawString(50, y, "Правила:")
        c.setFillColor(colors.blue)  # Фиолетовый цвет
        c.drawString(120, y, f"{game.Rules}")
        c.setFillColor(colors.black)  # Возвращаем черный цвет
        y -= line_height

    if y <= line_height:
        c.showPage()
        y = page_height - line_height

    # Завершение создания PDF документа
    c.save()
    pdf_bytes = buffer.getvalue()
    buffer.close()

    return pdf_bytes
