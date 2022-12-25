import csv
from time import sleep

import requests
from bs4 import BeautifulSoup
from pathos.multiprocessing import Pool
from transliterate import translit

requests.packages.urllib3.disable_warnings()


def get_html(url):
    sleep(0.1)
    r = requests.get(url, verify=False)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('../../../analyse/csv/gagagames.csv', 'a', encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['name_ga'],
                         data['image_ga'],
                         data['plus'],
                         data['feature'],
                         data['minus'],
                         data['resume'],
                         data['rules'],
                         data['url_game_ga'],
                         data['transliterated_name']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    games = soup.find_all('div', class_='preview-card')

    for game in games:
        try:
            name = game.find('p', class_='preview-card__title').find('a').get('title').strip()
        except:
            name = ''
        try:
            url_game_ga = 'https://gaga.ru' + game.find('p', class_='preview-card__title').find(
                'a').get('href')
        except:
            url_game_ga = ''
        try:
            game_inside = BeautifulSoup(get_html(url_game_ga), 'lxml')
        except:
            break
        try:
            image_ga = 'https://gaga.ru' + game_inside.find_all('img', itemprop='image')[-1].get('src')
        except:
            image_ga = ''
        try:
            pluses = game_inside.find_all('li', class_='plus-minus__item plus-minus__item--plus')
            plus = ''
            for i in range(0, len(pluses)):
                plus = plus + pluses[i].text.strip() + '^'
        except:
            plus = ''
        try:
            features = game_inside.find_all('li', class_='plus-minus__item plus-minus__item--features')
            feature = ''
            for i in range(0, len(features)):
                feature = feature + features[i].text.strip() + '^'
        except:
            feature = ''
        try:
            minuses = game_inside.find_all('li', class_='plus-minus__item plus-minus__item--minus')
            minus = ''
            for i in range(0, len(minuses)):
                minus = minus + minuses[i].text.strip() + '^'
        except:
            minus = ''
        try:
            resume = game_inside.find('section', class_='summary').find('p').text.strip()
        except:
            resume = ''
        try:
            rules = 'https://gaga.ru/' + game_inside.find('a', class_='btn-rules').get('href')
        except:
            rules = ''
        try:
            transliterated_name = translit(name, language_code='ru', reversed=True)
        except:
            transliterated_name = name

        data = {'name_ga': name,
                'plus': plus,
                'feature': feature,
                'minus': minus,
                'image_ga': image_ga,
                'resume': resume,
                'rules': rules,
                'url_game_ga': url_game_ga,
                'transliterated_name': transliterated_name

                }
        write_csv(data)


def make_all(url):
    text = get_html(url)
    get_page_data(text)


def main_parser():
    urls = list()
    url = 'https://gaga.ru/nastolnie-igri/'
    # get_page_data(get_html(url))
    urls.append(url)
    while True:
        try:
            soup = BeautifulSoup(get_html(url), 'lxml')
            url = 'https://gaga.ru/nastolnie-igri/' + soup.find('div', class_='gaga-pagination').find('div',
                                                                                                      string='»').find_parent().get(
                'href')
            urls.append(url)

        except:
            break

    columns = {'name_ga': 'Name_ga',
               'plus': 'Plus',
               'feature': 'Feature',
               'minus': 'Minus',
               'image_ga': 'Image_gaga',
               'resume': 'Resume',
               'rules': 'Rules',
               'url_game_ga': 'Url_game_gaga',
               'transliterated_name': 'Transliterated_name'}

    write_csv(columns)
    # make_all(url)
    with Pool(20) as p:
        p.map(make_all, urls)


if __name__ == '__main__':
    main_parser()
