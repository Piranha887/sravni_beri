import csv
from peewee import *

db = PostgresqlDatabase(database='SravniBeri', user='postgres', password='1234', host='localhost')


class GamesData(Model):
    Name = TextField()  # Имя должно быть одинаковым для всех
    Slogan = TextField()  # Берётся с HG
    Description = TextField()  # Берётся с Lavka
    Plus = TextField()  # Gaga
    Feature = TextField()  # Gaga
    Minus = TextField()  # Gaga
    Resume = TextField()  # Gaga
    Tags = TextField()  # HG
    Language = TextField()  # Lavka
    Equipment = TextField()  # HG
    Url_game_hg = TextField()
    Url_game_gaga = TextField()
    Url_game_lavka = TextField()
    Image_HG = TextField()
    Image_GA = TextField()
    Image_LI = TextField()
    Price = CharField()  # Берётся HG
    Player = CharField()
    Time = CharField()
    Age = CharField()
    Rating_bgg = CharField()  # Берётся Lavka
    Rating_tesera = CharField()
    Rules = TextField()  # Gaga
    Year = CharField()  # HG
    Manufacture = TextField()

    class Meta():
        database = db


class Buttons(Model):
    library_buttons = CharField()
    year_buttons = CharField()
    manufacture_buttons = CharField()
    age_buttons = CharField()
    player_buttons = CharField()

    class Meta():
        database = db


def main():
    db.connect()

    db.create_tables([GamesData])

    with open('analyse/merged_data_parsers.csv', encoding="utf-8") as f:
        order = ['Name', 'Image_HG', 'Slogan', 'Tags', 'Price', 'Player', 'Time', 'Age', 'Year', 'Manufacture',
                 'Equipment', 'Url_game_hg', 'Image_GA', 'Plus', 'Feature', 'Minus', 'Resume', 'Rules', 'Url_game_gaga',
                 'Description', 'Language', 'Image_LI', 'Rating_bgg', 'Rating_tesera', 'Url_game_lavka']
        reader = csv.DictReader(f, fieldnames=order)
        games = list(reader)

        with db.atomic():
            for index in range(1, len(games), 100):
                GamesData.insert_many(games[index:index + 100]).execute()

    db.create_tables([Buttons])
    with open('analyse/buttons.csv', encoding="utf-8") as f:
        order = ['library_buttons', 'year_buttons', 'manufacture_buttons', 'age_buttons', 'player_buttons']
        reader = csv.DictReader(f, fieldnames=order)
        buttons = list(reader)

        with db.atomic():
            for index in range(1, len(buttons), 100):
                Buttons.insert_many(buttons[index:index + 100]).execute()


if __name__ == '__main__':
    main()
