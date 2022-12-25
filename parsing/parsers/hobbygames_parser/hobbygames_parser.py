import csv
import re
from time import sleep

import requests
from bs4 import BeautifulSoup
from pathos.multiprocessing import Pool
from transliterate import translit


def get_html(url):
    sleep(0.3)
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def clear_text_tags(text):
    clear_map = {
        ord('\n'): ',',
        ord('\t'): ' ',
        ord('\r'): ' '
    }
    text = text.translate(clear_map)
    text = " ".join(text.split())
    text = re.sub(',{2,}', '', text)
    text = re.sub(', {1,}', ',', text)
    text = text.lstrip(',')
    return text


def clear_text_equipment(text):
    clear_map = {
        ord('\n'): ',',
        ord('\t'): ' ',
        ord('\r'): ' '
    }
    text = text.translate(clear_map)
    text = " ".join(text.split())
    text = re.sub(', {1,}', ',', text)
    text = re.sub(',,{1,}', ',', text)
    text = text.lstrip(',')
    return text


def write_csv(data):
    with open('../../../analyse/csv/hobbygames.csv', 'a', encoding="utf-8", newline='') as f:
        order = ['name_hg', 'image_hg', 'slogan', 'tags', 'price', 'player', 'time', 'age', 'year', 'manufacture',
                 'equipment', 'url_game_hg', 'transliterated_name']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    games = soup.find_all('div', class_='col-lg-4 col-md-6 col-sm-6 col-xs-12')

    for game in games:
        try:
            name = game.find('a', class_='name').get('title').strip()
        except:
            name = ''
        try:
            slogan = game.find('div', class_='desc').text.strip()
        except:
            slogan = ''
        try:
            url_game_hg = game.find('a', class_='name').get('href')
        except:
            url_game_hg = ''

        try:
            player = game.find('div', class_='params__item players').find('span').text
        except:
            player = ''
        try:
            time = game.find('div', class_='params__item time').find('span').text
        except:
            time = ''
        try:
            age = game.find('div', class_='params__item age').find('div', class_='age__number').text
        except:
            age = ''

        game_inside = BeautifulSoup(get_html(url_game_hg), 'lxml')

        try:
            image_hg = game_inside.find_all('img', itemprop='image')[0].get('data-src')
        except:
            image_hg = ''
        try:
            price = game_inside.find('div', class_='price-item').text.strip()
            price = price.replace('₽', '')
            price = price.replace(' ', '')
        except:
            price = ''
        try:
            tags = game_inside.find('div', class_='tags').text.strip()
            tags = clear_text_tags(tags)

        except:
            tags = ''
        try:
            year = game_inside.find('div', class_='manufacturers__value main-color').text.strip()
        except:
            year = ''
        try:
            manufacture = game_inside.find('a', class_='manufacturers__value main-color').text
        except:
            manufacture = ''
        try:
            equipment = game_inside.find('div', class_='desc-text collapsed').text.strip()
            equipment = clear_text_equipment(equipment)

        except:
            equipment = ''
        try:
            transliterated_name = translit(name, language_code='ru', reversed=True)
        except:
            transliterated_name = name

        data = {'name_hg': name,
                'image_hg': image_hg,
                'slogan': slogan,
                'tags': tags,
                'price': price,
                'player': player,
                'time': time,
                'age': age,
                'year': year,
                'manufacture': manufacture,
                'equipment': equipment,
                'url_game_hg': url_game_hg,
                'transliterated_name': transliterated_name}
        write_csv(data)


def make_all(url):
    text_html = get_html(url)
    get_page_data(text_html)


def main_parser():
    urls = list()
    url = 'https://hobbygames.ru/nastolnie'
    urls.append(url)
    while True:
        try:
            soup = BeautifulSoup(get_html(url), 'lxml')
            url = 'https://hobbygames.ru/nastolnie' + soup.find('ul', class_='pagination').find('a', class_='next').get(
                'href')
            urls.append(url)

        except:
            break

    columns = {'name_hg': 'Name_HG',  # название игры на HG
               'image_hg': 'Image_HG',  # первая по номеру картинка игры
               'slogan': 'Slogan',  # подпись к игре
               'tags': 'Tags',  # метки или жанры игры
               'price': 'Price',  # Цена игры
               'player': 'Player',  # Кол-во игроков для игры
               'time': 'Time',  # Примерное время игры
               'age': 'Age',  # Возрастное ограничение
               'year': 'Year',  # Год выпуска
               'manufacture': 'Manufacture',  # Производитель
               'equipment': 'Equipment',  # Комплектация
               'url_game_hg': 'Url_game_hg',  # Ссылка на игру в HG
               'transliterated_name': 'Transliterated_name'}  # не связан с парсингом
    write_csv(columns)

    with Pool(20) as p:
        p.map(make_all, urls)


if __name__ == '__main__':
    main_parser()
