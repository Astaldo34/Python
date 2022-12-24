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