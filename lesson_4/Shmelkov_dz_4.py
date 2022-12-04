# 1 Вычислить число π c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import *
import math

print("Задание №1")

# param_nums = int(input("Введите количество знаков после запятой у числа Pi: "))
param_nums = 5
param_d = 0.001

math_pi = Decimal(math.pi)
my_pi = Decimal(0)
i = Decimal(0)

while i < 1000:
    my_pi = my_pi + 1 / (16 ** i) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))
    i += 1

my_pi = round(my_pi, param_nums)
# print(round(math_pi, param_nums))
if (math_pi - my_pi) < param_d:
    print(f"Соответветсует системному числу Pi, значение - {my_pi}")
else:
    print("Не соответсвует...что-то пошло не так")

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]


print("Задание №2")
# param_nums = int(input("Введите число: "))
param_nums = 236


def multipliers(n):
    res_nums = []
    while n % 2 == 0:
        res_nums.append(2)
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            res_nums.append(i)
            n /= i
    if n > 2:
        res_nums.append(int(n))
    return res_nums


print(multipliers(param_nums))

# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]


print("Задание №3")
sample_list = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]

result_list = []
for i in sample_list:
    if sample_list.count(i) == 1:
        result_list.append(i)

print(result_list)

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randrange

print("Задание №4")
k = 2


def form_expression(k):
    result_expression = f'{randrange(101)}'
    for i in range(1, k + 1):
        result_expression += f' + {randrange(101)}*x**{i}'
    result_expression += f' = 0'
    return result_expression


print(form_expression(k))

# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму
# многочленов. Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.


print("Задание №5")

with open('first.txt', 'w+') as file_one:
    file_one.write(form_expression(k))

with open('two.txt', 'w+') as file_two:
    file_two.write(form_expression(k))

with open('first.txt', 'r') as file_one:
    first_string = file_one.read()

with open('two.txt', 'r') as file_two:
    two_string = file_two.read()

print(first_string)
print(two_string)

for i in first_string.split():
    if i.isdigit():
        print(i)
    if i.find('x') != -1:
        print(f'files - {i}')
    # Дальше не докрутил, нету сил уже...


