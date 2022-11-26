# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
#
# - 6782 -> 23
# - 0.56 -> 11


def sum_some_number():
    some_str = input("Введите вещественное число: ")
    sum_int = 0
    for i in some_str:
        if i.isdigit():
            sum_int += int(i)

    if sum_int == 0:
        print("Вы ввели значение, в котором нет цифр, попробуйте ещё раз")
        sum_some_number()
    else:
        return print(f"Сумма чисел числа равна - {sum_int}")


sum_some_number()

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Запрещено использовать функцию factorial из библиотеки math


some_int = int(input("Введите любое число: "))


def factorial_num(n):
    multi_list = []
    for i in range(1, n + 1):
        res = 1
        for num in range(1, i + 1):
            res *= num
        multi_list.append(res)
    return print(multi_list)


factorial_num(some_int)

# 3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
# *Пример:*
#
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

int_for_chain = int(input("Введите число для формирования суммы последовательности: "))

sum_chain = 0
for n in range(1, int_for_chain + 1):
    sum_chain += (1 + 1 / n) ** n

print(round(sum_chain, 3))

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции вводятся с клавиатуры.

import random

len_list = int(input("Введите длину массива: "))

random_list = []
for i in range(len_list):
    random_list.append(random.randint(-len_list, len_list + 1))

user_position_first = int(input("Введите позицию первого элемента: "))
user_position_two = int(input("Введите позицию второго элемента: "))

print(random_list)
print(random_list[user_position_first] * random_list[user_position_two])

# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

origin_list = [1, 2, 3, 4, 5, 6, 7, 8]


def randomaizer(list):
    new_list = []
    for i in range(0, len(list)):
        new_list.append(list.pop(random.randint(0, len(list) - 1)))
    return new_list


print(randomaizer(origin_list))
