def math_action(sample: str):
    arg_list = sample.split(' ')
    first_num = arg_list[0]
    two_num = arg_list[-1]

    if first_num.isdigit() and two_num.isdigit():
        first_num = float(first_num)
        two_num = float(two_num)
        if '+' in arg_list[1]:
            return f'{first_num} + {two_num} = {first_num + two_num}'
        elif '-' in arg_list[1]:
            return f'{first_num} - {two_num} = {first_num - two_num}'
        elif '*' in arg_list[1]:
            return f'{first_num} * {two_num} = {first_num * two_num}'
        elif '/' in arg_list[1]:
            if two_num == 0:
                return "Делить на 0 нельзя"
            return f'{first_num} / {two_num} = {first_num / two_num}'
        else:
            return "Введены не корректные символы, попробуйте ещё раз"
    else:
        return "Введены не корректные значения, попробуйте ещё раз"


first_clx = 0j
two_clx = 0j
sign_clx = ''


def math_action_1(sign: str):
    global sign_clx
    if '+' in sign:
        sign_clx = '+'
        return sign_clx
    elif '-' in sign:
        sign_clx = '-'
        return sign_clx
    elif '*' in sign:
        sign_clx = '*'
        return sign_clx
    elif '/' in sign:
        sign_clx = '/'
        return sign_clx
    else:
        return "Введено не комплексное число или не верного формата. Используйте выражение типа '3 + 7j'"


def math_action_2(first: str):
    try:
        global first_clx
        first_clx = complex(first.replace(' ', ''))

    except ValueError:
        return "Введено не комплексное число или не верного формата. Используйте выражение типа '3 + 7j'"


def math_action_3(two: str):
    try:
        global two_clx
        two_clx = complex(two.replace(' ', ''))
        if sign_clx == "+":
            result_clx = first_clx + two_clx
        elif sign_clx == "-":
            result_clx = first_clx - two_clx
        elif sign_clx == "*":
            result_clx = first_clx * two_clx
        elif sign_clx == "/":
            result_clx = first_clx / two_clx
        else:
            result_clx = None
        return f'Результат: {first_clx} {sign_clx} {two_clx} = {result_clx}'
    except ValueError:
        return "Введено не комплексное число или не верного формата. Используйте выражение типа '3 + 7j'"


# print("Выберите нужную операцию ('+','-','*','/'): ")
# math_action_1('+')
