# 3 Создайте программу для игры в "Крестики-нолики".
# Вариант интерфейса:
#
#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9

from random import randrange


field = {
    '1': ':one:',
    '2': ':two:',
    '3': ':three:',
    '4': ':four:',
    '5': ':five:',
    '6': ':six:',
    '7': ':seven:',
    '8': ':eight:',
    '9': ':nine:'
}


def field_drawing(x=0):
    if x != 0:
        field[str(x)] = ':green_circle:'
        position_o = str(randrange(1, 10))
        while field[position_o] == ':green_circle:' or field[position_o] == ':x:':
            position_o = str(randrange(1, 10))
        field[position_o] = ':x:'
    fld = f'| {field["1"]} | {field["2"]} | {field["3"]} |\n' \
          f'_________________\n' \
          f'| {field["4"]} | {field["5"]} | {field["6"]} |\n' \
          f'_________________\n' \
          f'| {field["7"]} | {field["8"]} | {field["9"]} |'
    return fld


# field_drawing()


def game_x_o(step=0):
    if (field['1'] == ':green_circle:' and field['2'] == ':green_circle:' and field['3'] == ':green_circle:') or \
            (field['4'] == ':green_circle:' and field['5'] == ':green_circle:' and field['6'] == ':green_circle:') or \
            (field['7'] == ':green_circle:' and field['8'] == ':green_circle:' and field['9'] == ':green_circle:') or \
            (field['1'] == ':green_circle:' and field['4'] == ':green_circle:' and field['7'] == ':green_circle:') or \
            (field['2'] == ':green_circle:' and field['5'] == ':green_circle:' and field['8'] == ':green_circle:') or \
            (field['3'] == ':green_circle:' and field['6'] == ':green_circle:' and field['9'] == ':green_circle:') or \
            (field['3'] == ':green_circle:' and field['5'] == ':green_circle:' and field['7'] == ':green_circle:') or \
            (field['1'] == ':green_circle:' and field['5'] == ':green_circle:' and field['9'] == ':green_circle:'):
        return "Вы выиграли! :sunglasses:"
    if (field['1'] == ':x:' and field['2'] == ':x:' and field['3'] == ':x:') or \
            (field['4'] == ':x:' and field['5'] == ':x:' and field['6'] == ':x:') or \
            (field['7'] == ':x:' and field['8'] == ':x:' and field['9'] == ':x:') or \
            (field['1'] == ':x:' and field['4'] == ':x:' and field['7'] == ':x:') or \
            (field['2'] == ':x:' and field['5'] == ':x:' and field['8'] == ':x:') or \
            (field['3'] == ':x:' and field['6'] == ':x:' and field['9'] == ':x:') or \
            (field['3'] == ':x:' and field['5'] == ':x:' and field['7'] == ':x:') or \
            (field['1'] == ':x:' and field['5'] == ':x:' and field['9'] == ':x:'):
        return "Вы проиграли :cry:"
    if step >= 5:
        return "Игра закончена :blush:"
    return 'next'


# game_x_o()
