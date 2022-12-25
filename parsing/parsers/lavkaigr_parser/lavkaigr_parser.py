import csv
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


def clear_text(text):
    text = ' '.join(text)
    clear_map = {
        ord('\n'): ' ',
        ord('\t'): ' ',
        ord('\r'): ' '
    }
    return text.translate(clear_map)


def write_csv(data):
    with open('../../../analyse/csv/lavkaigr.csv', 'a', encoding="utf-8", newline='') as f:
        order = ['name_li', 'desc', 'language', 'image_li', 'rating_bgg', 'rating_tesera', 'url_game_li',
                 'transliterated_name']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    games = soup.find_all('div', class_='block')
    for game in games:
        try:
            url_game_li = 'https://www.lavkaigr.ru/shop/nastolnye-igry/' + \
                          game.find('a', class_='game-name').get('href')
        except:
            url_game_li = ''

        try:
            game_inside = BeautifulSoup(get_html(url_game_li), 'lxml')
        except:
            break

        try:
            name = game_inside.find('h2', class_='game-name').text.strip()
        except:
            name = ''

        try:
            desc = game_inside.find('div', itemprop='description').find_all(text=True)
            desc = clear_text(desc)

        except:
            desc = ''
        try:
            language = game_inside.find('i', class_='fa fa-language') \
                .find_parent().find_parent().find('strong').text.strip()
        except:
            language = ''
        try:
            image_li = game_inside.find('div', class_="thumbs tobo").find_all('img')[-1].find_parent().get(
                'href').strip()
        except:
            image_li = ''
        try:
            rating_bgg = game_inside.find('p', string='BGG').find_parent().find('div', class_='block-tbl wtd100').find(
                'div').find('span').text.strip()
            rating_bgg = rating_bgg.replace(',', '.')
        except:
            rating_bgg = ''
        try:
            rating_tesera = game_inside.find('p', string='Тесера').find_parent().find('div',
                                                                                      class_='block-tbl wtd100').find(
                'div').find('span').text.strip()
            rating_tesera = rating_tesera.replace(',', '.')
        except:
            rating_tesera = ''
        try:
            transliterated_name = translit(name, language_code='ru', reversed=True)
        except:
            transliterated_name = name

        data = {'name_li': name,
                'desc': desc,
                'language': language,
                'image_li': image_li,
                'rating_bgg': rating_bgg,
                'rating_tesera': rating_tesera,
                'url_game_li': url_game_li,
                'transliterated_name': transliterated_name}
        write_csv(data)


def make_all(url):
    text_html = get_html(url)
    get_page_data(text_html)


def main_parser():
    urls = list()
    url = 'https://www.lavkaigr.ru/shop/nastolnye-igry/'
    urls.append(url)

    while True:
        try:
            soup = BeautifulSoup(get_html(url), 'lxml')
            url = 'https://www.lavkaigr.ru/shop/nastolnye-igry/' + soup.find('li', class_='next').find('a').get(
                'href')
            urls.append(url)

        except:
            break

    columns = {'name_li': 'Name_LI',
               'desc': 'Description',
               'language': 'Language',
               'image_li': 'Image_lavka',
               'rating_bgg': 'Rating_bgg',
               'rating_tesera': 'Rating_tesera',
               'url_game_li': 'Url_game_lavka',
               'transliterated_name': 'Transliterated_name'
               }

    write_csv(columns)

    with Pool(20) as p:
        p.map(make_all, urls)


if __name__ == '__main__':
    main_parser()
