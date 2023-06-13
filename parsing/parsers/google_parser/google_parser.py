import csv
from time import sleep
import requests
from bs4 import BeautifulSoup

USER_AGENT = \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"User-Agent": USER_AGENT}


# Функция для получения HTML-кода страницы по указанному URL
def get_html(url):
    sleep(0.3)  # Задержка 0.3 секунды для этического парсинга
    r = requests.get(url, headers=headers)  # Отправка GET-запроса по указанному URL с заголовками
    if r.ok:  # Если получен ответ со статусом 200 (OK)
        return r.text  # Возвращается HTML-код страницы
    print(r.status_code)  # В противном случае выводится статус-код ответа (ошибка)


# Функция для получения данных со страницы
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')  # Создание объекта BeautifulSoup для анализа HTML-кода
    links = list()  # Создание пустого списка для хранения ссылок
    titles = soup.find_all('h3')  # Поиск всех элементов с тегом 'h3' на странице
    titles = titles[:5]  # Ограничение списка заголовков до первых 5 элементов
    for title in titles:  # Для каждого заголовка
        links.append(title.find_parent().get(
            'href'))  # Получение ссылки из родительского элемента заголовка и добавление её в список
    return links  # Возвращается список ссылок


# Функция для анализа ссылок и проверки их наличия в файлах CSV
def analyse_links(links_hg, links_li):
    t = False  # Флаг, указывающий, найдены ли совпадения ссылок
    links = list()  # Создание пустого списка для хранения найденных ссылок
    with open('../../../analyse/csv/hobbygames.csv', 'r', encoding='utf-8', errors='ignore', newline='') as f:
        reader = csv.DictReader(f)  # Создание объекта чтения CSV-файла
        for link in links_hg:  # Для каждой ссылки на игру из списка ссылок hobbygames
            if t:  # Если уже найдено совпадение
                break  # Прервать цикл
            for row in reader:  # Для каждой строки CSV-файла
                # Если ссылка на игру совпадает со значением столбца 'Url_game_hg' текущей строки
                if link == row['Url_game_hg']:
                    t = True  # Установить флаг совпадения в True
                    links.append(link)  # Добавить ссылку в список найденных ссылок
                    break  # Прервать цикл
    if t:  # Если найдены совпадения ссылок
        t = False  # Сбросить флаг совпадения в False
        with open('../../../analyse/csv/lavkaigr.csv', 'r', encoding='utf-8', errors='ignore', newline='') as f:
            reader = csv.DictReader(f)  # Создание объекта чтения CSV-файла
            for link in links_li:  # Для каждой ссылки на игру из списка ссылок lavkaigr
                if t:  # Если уже найдено совпадение
                    break  # Прервать цикл
                for row in reader:  # Для каждой строки CSV-файла
                    # Если ссылка на игру совпадает со значением столбца 'Url_game_lavka' текущей строки
                    if link == row['Url_game_lavka']:
                        t = True  # Установить флаг совпадения в True
                        links.append(link)  # Добавить ссылку в список найденных ссылок
                        break  # Прервать цикл
    if t:  # Если найдены совпадения ссылок
        return links  # Возвращается список найденных ссылок
    else:
        return False  # Если совпадений ссылок не найдено, возвращается значение False


# Функция для чтения названий игр из файла gagagames.csv
def read_gaga_names(array_gaga_names):
    with open('../../../analyse/csv/gagagames.csv', 'r', encoding='utf-8', errors='ignore', newline='') as f:
        reader = csv.DictReader(f)  # Создание объекта чтения CSV-файла
        for row in reader:  # Для каждой строки CSV-файла
            # Добавление значения столбца 'Name_ga' в список названий игр
            array_gaga_names.append(str(row['Name_ga']))
        return array_gaga_names  # Возвращается список названий игр


# Функция для очистки названий игр от лишних символов
def clear_names(array_hg_names):
    clear_map = {
        ord(' '): '+'  # Определение отображения символа пробела на символ плюса
    }
    # Применение отображения символов на строку с использованием метода translate()
    text = array_hg_names.translate(clear_map)
    return text  # Возвращается очищенная строка названия игры


# Функция для записи данных в файл merged_links.csv
def write_csv(data):
    with open('../../../analyse/csv/merged_links.csv', 'a', encoding="utf-8", newline='') as f:
        order = ['Name_ga', 'Url_game_hg', 'Url_game_li']  # Определение порядка столбцов
        writer = csv.DictWriter(f, fieldnames=order)  # Создание объекта для записи CSV-файла
        writer.writerow(data)  # Запись данных в CSV-файл по заданным столбцам


# Основная функция парсинга
def main_parser():
    array_gaga_names = []  # Создание пустого списка для хранения названий игр
    array_gaga_names = \
        read_gaga_names(array_gaga_names)  # Получение названий игр из файла CSV и сохранение их в списке
    array_gaga_names_old = array_gaga_names  # Создание копии списка названий игр
    array_gaga_names = [word.replace(' ', '+') for word in
                        array_gaga_names]  # Замена пробелов на плюсы в каждом названии игры

    columns = {
        'Name_ga': 'Name_ga',
        'Url_game_hg': 'Url_game_hg',
        'Url_game_li': 'Url_game_lavka'
    }
    write_csv(columns)  # Запись заголовков столбцов в файл CSV

    i = 0  # Инициализация счетчика
    for word in array_gaga_names:  # Для каждого названия игры в списке
        url_hg = 'https://www.google.ru/search?q=' + word \
                 + '+hobbygames'  # Формирование URL для поиска в Google (hobbygames)
        url_li = 'https://www.google.ru/search?q=' + word \
                 + '+lavkaigr'  # Формирование URL для поиска в Google (lavkaigr)

        links = analyse_links(get_page_data(get_html(url_hg)),
                              get_page_data(get_html(url_li)))  # Получение ссылок на игры из результатов поиска

        if links:  # Если есть ссылки на игры
            data = {
                'Name_ga': array_gaga_names_old[i],
                'Url_game_hg': links[0],
                'Url_game_li': links[1]
            }
            write_csv(data)  # Запись данных в файл CSV
        i += 1  # Увеличение счетчика


if __name__ == '__main__':
    main_parser()
