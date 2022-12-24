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