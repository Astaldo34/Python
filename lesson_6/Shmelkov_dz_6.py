
print("Задание №1 - старое")
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

some_list_one = [2, 3, 5, 9, 3]

sum_elem = 0
for item in some_list_one[1::2]:
    sum_elem += item

print(f'Сумма элементов на нечётной позиции равна - {sum_elem}')

print("Задание №1 - ! новое")

sum_elem = sum(map(lambda x: x, some_list_one[1::2]))

print(f'Сумма элементов на нечётной позиции равна - {sum_elem}')

print("\nЗадание №2 - старое")

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
# последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

sample_list = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]

result_list = []
for i in sample_list:
    if sample_list.count(i) == 1:
        result_list.append(i)

print(result_list)

print("Задание №2 - ! новое")

result_list = list(x for x in sample_list if sample_list.count(x) == 1)

print(result_list)


print("\nЗадание №3 - старое")

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

comp_dublet = []
some_list_two = [2, 3, 4, 5, 6]

for i in range(len(some_list_two)):
    if i >= len(some_list_two) / 2:
        break
    comp_dublet.append(some_list_two[i] * some_list_two[-1 - i])

print(f'произведение пар чисел списка - {comp_dublet}')

print("Задание №3 - ! новое")

comp_dublet = []
some_list_two = [2, 3, 4, 5, 6]

for index, value in enumerate(some_list_two):
    if index >= len(some_list_two) / 2:
        break
    comp_dublet.append(value * some_list_two[-1 - index])

print(f'произведение пар чисел списка - {comp_dublet}')

print("\nЗадание №4 - старое") # Уже использованы

# 1 Напишите программу, удаляющую из файла все слова, содержащие "абв".


first_string = "абв кулибяка варилась в скабвародке"

result_string = filter(lambda x: 'абв' not in x, first_string.split())
print(*result_string)

print("Задание №4 - ! новое уже использованы функции")


