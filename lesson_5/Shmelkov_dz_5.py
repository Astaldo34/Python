# 1 Напишите программу, удаляющую из файла все слова, содержащие "абв".


print("Задание №1")

first_string = "абв кулибяка варилась в скабвародке"

result_string = filter(lambda x: 'абв' not in x, first_string.split())
print(*result_string)

# 2 Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


print("Задание №2")

from random import randrange

print("Начало игры")
my_move = randrange(0, 2)
# candies = 2021
candies = 201


def steps_game(cand:int, who='p1'):
    if who == 'p1':
        my_steps = int(input(f'Всего осталось {cand} конфет, сколько возьмёте конфет от 1 до 28? '))
        while my_steps > 28 or my_steps > cand:
            print("Вы ввели не верное значение, попробуйте ещё раз")
            my_steps = int(input(f'Всего осталось {cand} конфет, сколько возьмёте конфет от 1 до 28? '))
        cand -= my_steps
        if cand == 0:
            return print('Вы выиграли !')
        print(f'Вы взяли {my_steps} конфет, осталось {cand}')

    comp_steps = randrange(1, 29)
    if cand <= 28:
        comp_steps = 28
    elif cand <= 28 * 2 + 1:
        comp_steps = cand - 29
    elif 84 < cand < 28 * 2 + 1:
        comp_steps = 1
    else:
        while comp_steps > 28 or comp_steps > cand:
            comp_steps = randrange(1, 29)
    cand -= comp_steps
    print(f'Соперник взял {comp_steps} конфет, осталось {cand}')
    if cand <= 0:
        return print('Вы проиграли :(')
    steps_game(cand, 'p1')


if my_move:
    print("Вы ходите первым!")
    steps_game(candies, 'p1')
else:
    print("Соперник ходит первым")
    steps_game(candies, 'p2')


# 3 Создайте программу для игры в "Крестики-нолики".
# Вариант интерфейса:
#
#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9


print("Задание №3")

field = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def field_drawing(x=0):
    if x != 0:
        field[str(x)] = 'X'
        position_o = str(randrange(1, 10))
        while field[position_o] == 'X' or field[position_o] == 'O':
            position_o = str(randrange(1, 10))
        field[position_o] = 'O'
    print(f'| {field["1"]} | {field["2"]} | {field["3"]} |')
    print(f'_____________')
    print(f'| {field["4"]} | {field["5"]} | {field["6"]} |')
    print(f'_____________')
    print(f'| {field["7"]} | {field["8"]} | {field["9"]} |')
    print(f'_____________')


field_drawing()


def game_x_o(step=0):
    if (field['1'] == 'X' and field['2'] == 'X' and field['3'] == 'X') or \
            (field['4'] == 'X' and field['5'] == 'X' and field['6'] == 'X') or \
            (field['7'] == 'X' and field['8'] == 'X' and field['9'] == 'X') or \
            (field['1'] == 'X' and field['4'] == 'X' and field['7'] == 'X') or \
            (field['2'] == 'X' and field['5'] == 'X' and field['8'] == 'X') or \
            (field['3'] == 'X' and field['6'] == 'X' and field['9'] == 'X') or \
            (field['3'] == 'X' and field['5'] == 'X' and field['7'] == 'X') or \
            (field['1'] == 'X' and field['5'] == 'X' and field['9'] == 'X'):
        return print("Вы выиграли!!!")
    if (field['1'] == 'O' and field['2'] == 'O' and field['3'] == 'O') or \
            (field['4'] == 'O' and field['5'] == 'O' and field['6'] == 'O') or \
            (field['7'] == 'O' and field['8'] == 'O' and field['9'] == 'O') or \
            (field['1'] == 'O' and field['4'] == 'O' and field['7'] == 'O') or \
            (field['2'] == 'O' and field['5'] == 'O' and field['8'] == 'O') or \
            (field['3'] == 'O' and field['6'] == 'O' and field['9'] == 'O') or \
            (field['3'] == 'O' and field['5'] == 'O' and field['7'] == 'O') or \
            (field['1'] == 'O' and field['5'] == 'O' and field['9'] == 'O'):
        return print("Вы проиграли :(")
    if step >= 5:
        return print("Игра закончена")
    user_position = int(input("Введите позицию, на которую хотите сделать ход (от 1 до 9): "))
    if user_position > 9 or user_position < 1:
        print("Вы ввели не допустимое значение")
        game_x_o()
    field_drawing(user_position)
    step += 1
    game_x_o(step)


game_x_o()

# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff


print("Задание №4")

# Создание файла с заданной строкой
some_text = 'aaaasssdddwwwwwwwwwwwweeeffffff'

with open('input.txt', 'w+') as fl:
    fl.write(some_text)

with open('input.txt', 'r') as fl:
    input_string = list(fl.read())

# print(input_string)
out_list = []


def rle(lst: list, ind=0):
    if lst.count(lst[ind]) > 9:
        out_list.append(f'9{lst[ind]}')
        out_list.append(f'{lst.count(lst[ind]) - 9}{lst[ind]}')
    else:
        out_list.append(f'{lst.count(lst[ind])}{lst[ind]}')
    if len(lst) - 1 > ind + lst.count(lst[ind]):
        rle(input_string, ind + lst.count(lst[ind]))
    return out_list


res_string = "".join(rle(input_string))
print(res_string)

with open('out.txt', 'w+') as fl:
    fl.write(res_string)

# Восстановление данных

original_str = ''
num = 0
for i in res_string:
    if i.isdigit():
        num = int(i)
    else:
        n = 0
        while n < num:
            original_str += i
            n += 1

print(original_str)

# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.
#
# Пример:
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


print("Задание №5")
fst_example = [1, 5, 2, 3, 4, 6, 1, 7]
result = []


def long_list(lst:list, num=0):
    for inx, item in enumerate(lst):
        if item > num:
            # print(len([x for x in lst[inx:] if x < item]))
            if len([x for x in lst[inx:] if x < item]) <= 2:
                result.append(item)
                num = item
        # long_list(lst, i)


long_list(fst_example)
print(result)
