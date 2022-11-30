# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print("Задание №1")
some_list_one = [2, 3, 5, 9, 3]

sum_elem = 0
for item in some_list_one[1::2]:
    sum_elem += item

print(f'Сумма элементов на нечётной позиции равна - {sum_elem}')


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


print("Задание №2")

comp_dublet = []
some_list_two = [2, 3, 4, 5, 6]

for i in range(len(some_list_two)):
    if i >= len(some_list_two) / 2:
        break
    comp_dublet.append(some_list_two[i] * some_list_two[-1 - i])

print(f'произведение пар чисел списка - {comp_dublet}')


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


print("Задание №3")

some_list_three = [1.1, 1.2, 3.1, 5, 10.01]

min_part = 99
max_part = 0
for item in some_list_three:
    # print(str(item).split('.')[1])
    part = round(item - int(item), 2)
    if min_part > part != 0:
        min_part = part
    if max_part < part != 0:
        max_part = part

print(max_part - min_part)


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


print("Задание №4")


def num_for_binary(num):
    res = []
    while num != 0:
        res.append(num % 2)
        num = num // 2

    res.reverse()
    print(*res)


num_for_binary(45)
num_for_binary(2)


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


print("Задание №5")

# не разобрался с отрицательными

def fibo(len_lst):
    res_list = [0, 1]
    for i in range(1, len_lst):
        sum_el = res_list[i-1] + res_list[i]
        res_list.append(sum_el)
    return res_list


print(fibo(8))