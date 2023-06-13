import csv
import os

from peewee import *

# Подключение к базе данных PostgreSQL
db = PostgresqlDatabase(database=str(os.getenv("DATABASE")), user=str(os.getenv("PGUSER")),
                        password=str(os.getenv("PGPASSWORD")), host='localhost')


# Определение модели GamesData
class GamesData(Model):
    Name = TextField()  # Имя должно быть одинаковым для всех
    Url_game_hg = TextField()
    Url_game_lavka = TextField()
    Image_HG = TextField()
    Slogan = TextField()  # Берётся с HG
    Tags = TextField()  # Берётся с HG
    Price = CharField()  # Берётся с HG
    Player = CharField()  # Берётся с HG
    Time = CharField()  # Берётся с HG
    Age = CharField()  # Берётся с HG
    Year = CharField()  # Берётся с HG
    Manufacture = TextField()  # Берётся с HG
    Equipment = TextField()  # Берётся с HG
    Description = TextField()  # Берётся с LI
    Language = TextField()  # Берётся с LI
    Image_lavka = TextField()  # Берётся с LI
    Rating_bgg = CharField()  # Берётся с LI
    Rating_tesera = CharField()  # Берётся с LI
    Image_gaga = TextField()  # Берётся с Gaga
    Plus = TextField()  # Берётся с Gaga
    Feature = TextField()  # Берётся с Gaga
    Minus = TextField()  # Берётся с Gaga
    Resume = TextField()  # Берётся с Gaga
    Rules = TextField()  # Берётся с Gaga
    Url_game_gaga = TextField()

    class Meta():
        database = db


# Определение модели Buttons
class Buttons(Model):
    library_buttons = CharField()
    year_buttons = CharField()
    manufacture_buttons = CharField()
    age_buttons = CharField()
    player_buttons = CharField()

    class Meta():
        database = db


def main():
    # Подключение к базе данных
    db.connect()

    # Создание таблицы GamesData
    db.create_tables([GamesData])

    # Чтение данных из файла merged_data_parsers.csv
    with open('analyse/merged_data_parsers.csv', encoding="utf-8") as f:
        order = ['Name', 'Url_game_hg', 'Url_game_lavka', 'Image_HG', 'Slogan', 'Tags', 'Price', 'Player',
                 'Time', 'Age', 'Year', 'Manufacture', 'Equipment', 'Description', 'Language', 'Image_lavka',
                 'Rating_bgg', 'Rating_tesera', 'Image_gaga', 'Plus', 'Feature', 'Minus', 'Resume', 'Rules',
                 'Url_game_gaga']
        reader = csv.DictReader(f, fieldnames=order)
        games = list(reader)

        # Вставка данных в таблицу GamesData
        with db.atomic():
            for index in range(1, len(games), 100):
                GamesData.insert_many(games[index:index + 100]).execute()

    # Создание таблицы Buttons
    db.create_tables([Buttons])

    # Чтение данных из файла buttons.csv
    with open('analyse/buttons.csv', encoding="utf-8") as f:
        order = ['library_buttons', 'year_buttons', 'manufacture_buttons', 'age_buttons', 'player_buttons']
        reader = csv.DictReader(f, fieldnames=order)
        buttons = list(reader)

        # Вставка данных в таблицу Buttons
        with db.atomic():
            for index in range(1, len(buttons), 100):
                Buttons.insert_many(buttons[index:index + 100]).execute()


if __name__ == '__main__':
    main()
