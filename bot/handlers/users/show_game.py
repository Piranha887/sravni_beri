from aiogram.utils.markdown import hbold, hitalic, hlink


def empty_check(string, data):
    if (data != ''):
        return string + data
    else:
        return ''


def show_game(game):
    show = "\n".join([
        "\U0001f3b2 " +
        hbold(game.Name) +
        " \U0001f3b2\n" +
        hitalic(game.Slogan) +
        "\n\u0023\u20e3Тэги: " +
        game.Tags +
        "\nЯзык: " +
        game.Language +
        "\n\U0001f465Количество игроков: " +
        game.Player +
        "\n\u23f0Время игры: " +
        game.Time + " мин." +
        "\nВозрастное ограничение: " +
        game.Age +
        empty_check("\nРейтинг BGG: ", game.Rating_bgg) +
        empty_check("\nРейтинг Tesera: ", game.Rating_tesera) +
        f"\nЦена: {game.Price} ₽" +
        empty_check("\n\u2795Плюсы:\n", game.Plus.replace('^', '\n')) +
        empty_check("\n\u2796Минусы:\n", game.Minus.replace('^', '\n')) +
        empty_check("\n\u2611Особенности:\n", game.Feature.replace('^', '\n')) +
        "\nОписание:\n" +
        game.Description +
        empty_check("\nРезюме:\n", game.Resume) +
        "\nКомплектация:\n" +
        game.Equipment +
        hlink('\nСсылка на игру в HobbyGames', game.Url_game_hg) +
        hlink('\nСсылка на игру в GagaGames', game.Url_game_gaga) +
        hlink('\nСсылка на игру в LavkaIgr', game.Url_game_lavka) +
        hlink('\nПравила', game.Rules) +
        "\nГод: " +
        game.Year +
        "\nПроизводитель: " +
        game.Manufacture
    ]

    )
    return show
