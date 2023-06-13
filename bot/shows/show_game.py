# Импорт функций hbold, hitalic, hlink из модуля aiogram.utils.markdown
from aiogram.utils.markdown import hbold, hitalic, hlink


# Определение функции empty_check с параметрами string и data
def empty_check(string, data):
    # Проверка, если data не пустая строка
    if (data != ''):
        # Возвращение строки string + data
        return string + data
    else:
        # Возвращение пустой строки
        return ''


# Определение функции show_game с параметром game
def show_game(game):
    # Формирование переменной description с учетом условия
    description = game.Description[:2700] + f" ...\n\n[продолжение по ссылке в" + hlink('\n LavkaIgr',
                                                                                        game.Url_game_lavka) + "]" if len(
        game.Description) > 2700 else game.Description

    # Формирование переменной show с помощью метода join и списка строк
    show = "\n".join([
        "🎲 " +
        hbold(game.Name) +
        " 🎲\n" +
        hitalic(game.Slogan) +
        "\n#️⃣ Тэги: " +
        game.Tags +
        "\n🌐 Язык: " +
        game.Language +
        "\n👥 Количество игроков: " +
        game.Player +
        "\n⏰ Время игры: " +
        game.Time + " мин." +
        "\n🔞 Возрастное ограничение: " +
        game.Age +
        empty_check("\n🔵 Рейтинг BGG: ", game.Rating_bgg) +
        empty_check("\n🔵 Рейтинг Tesera: ", game.Rating_tesera) +
        f"\n💰 Цена: {game.Price} ₽ [взята по ссылке" + hlink('\nHobbyGames', game.Url_game_hg) + "]" +
        empty_check("\n✅ Плюсы:\n      ", game.Plus.replace('^', '\n      ')) +
        empty_check("\n❌ Минусы:\n     ", game.Minus.replace('^', '\n     ')) +
        empty_check("\n⭐ Особенности:\n      ", game.Feature.replace('^', '\n     ')) +
        "\n📝 Описание:\n" +
        description +
        empty_check("\n📄 Резюме:\n", game.Resume) +
        "\n📦 Комплектация:\n" +
        game.Equipment +
        hlink('\nСсылка на игру в HobbyGames', game.Url_game_hg) +
        hlink('\nСсылка на игру в GagaGames', game.Url_game_gaga) +
        hlink('\nСсылка на игру в LavkaIgr', game.Url_game_lavka) +
        hlink('\nПравила', game.Rules) +
        "\n📅 Год: " +
        game.Year +
        "\n⚙️ Производитель: " +
        game.Manufacture
    ])

    # Возвращение переменной show
    return show
