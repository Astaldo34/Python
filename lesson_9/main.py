from telebot import TeleBot, types
import emojis
import os

import record_log as rl
import game_1
import calc
import phone_book.book as bk
# import shutil

TOKEN = '5761290203:AAGeofxSfp_Ixl0APVg9yz1RqAdsrxbz-DE'

bot = TeleBot(TOKEN)


def m_menu():
    keyboard = types.InlineKeyboardMarkup()  # клавиатура
    game_1_but = types.InlineKeyboardButton(text='Игра "Крестики-нолики"', callback_data='game_1')
    keyboard.add(game_1_but)  # кнопка в клавиатуре
    calc_but = types.InlineKeyboardButton(text='Калькулятор', callback_data='calc')
    keyboard.add(calc_but)
    phone_but = types.InlineKeyboardButton(text='Телефонная книга', callback_data='phone')
    keyboard.add(phone_but)
    return keyboard


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    m_menu()
    # keyboard = types.InlineKeyboardMarkup()  # клавиатура
    # game_1_but = types.InlineKeyboardButton(text='Игра "Крестики-нолики"', callback_data='game_1')
    # keyboard.add(game_1_but)  # кнопка в клавиатуре
    # calc_but = types.InlineKeyboardButton(text='Калькулятор', callback_data='calc')
    # keyboard.add(calc_but)
    # phone_but = types.InlineKeyboardButton(text='Телефонная книга', callback_data='phone')
    # keyboard.add(phone_but)
    bot.send_message(msg.from_user.id, text="Выбери нужный пункт", reply_markup=m_menu())
    # bot.send_message(chat_id=msg.from_user.id, text=f'Введите арифметическую операцию \n{" ".join(lst)}')


@bot.message_handler(commands=['log'])
def log(msg: types.Message):
    bot.send_document(chat_id=msg.from_user.id, document=open('log.txt', 'r'))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "game_1":
        bot.send_message(chat_id=call.message.chat.id, text='Запускаю игру...')
        rl.add_log('Запускаю игру...')
        bot.send_message(chat_id=call.message.chat.id, text=emojis.encode(game_1.field_drawing()))
        bot.send_message(chat_id=call.message.chat.id, text='Введите позицию, '
                                                            'на которую хотите сделать ход (от 1 до 9):')
        rl.add_log('Введите позицию, на которую хотите сделать ход (от 1 до 9):')
        bot.register_next_step_handler(call.message, run_game)
    elif call.data == "calc":
        menu_calc = types.InlineKeyboardMarkup()
        calc_rac_but = types.InlineKeyboardButton(text='Рациональные', callback_data='calc_rac')
        menu_calc.add(calc_rac_but)
        calc_complex_but = types.InlineKeyboardButton(text='Комплексные', callback_data='calc_complex')
        menu_calc.add(calc_complex_but)
        bot.send_message(call.message.chat.id, text="Выберите с какими числами хотите работать", reply_markup=menu_calc)
    elif call.data == "calc_rac":
        bot.send_message(chat_id=call.message.chat.id, text='Введите выражение типа "3 + 8" или "10 / 2" через пробел')
        rl.add_log('Введите выражение типа "3 + 8" или "10 / 2" через пробел')
        bot.register_next_step_handler(call.message, calculator)
    elif call.data == "calc_complex":
        bot.send_message(chat_id=call.message.chat.id, text='Введите знак необходимой операции ("+", "-", "*", "/")')
        rl.add_log('Введите знак необходимой операции ("+", "-", "*", "/")')
        bot.register_next_step_handler(call.message, calculator_clx)
    elif call.data == "phone":
        menu_phone = types.InlineKeyboardMarkup()
        calc_rac_but = types.InlineKeyboardButton(text='Добавить контакт вручную', callback_data='phone_add')
        menu_phone.add(calc_rac_but)
        calc_complex_but = types.InlineKeyboardButton(text='Загрузить записи файлом', callback_data='phone_import')
        menu_phone.add(calc_complex_but)
        calc_complex_but = types.InlineKeyboardButton(text='Получить записи в файле', callback_data='phone_export')
        menu_phone.add(calc_complex_but)
        bot.send_message(call.message.chat.id, text="Выберите нужный пункт меню", reply_markup=menu_phone)
    elif call.data == "phone_add":
        bot.send_message(chat_id=call.message.chat.id, text='Введите ФИО, номер телефона и заметки. Важно использовать'
                                                            ' разделитель. Пример "Иванов Иван; 123-456-789-00; кто-то')
        rl.add_log('Введите ФИО, номер телефона и заметки. Важно использовать разделитель. Пример "Иванов Иван;'
                   ' 123-456-789-00; кто-то')
        bot.register_next_step_handler(call.message, phone_add)
    elif call.data == "phone_import":
        bot.send_message(chat_id=call.message.chat.id, text='Загрузите файл с данными')
        rl.add_log('Загрузите файл с данными в формате .xml')
    elif call.data == "phone_export":
        bot.send_message(chat_id=call.message.chat.id, text='Файл выслан')
        rl.add_log('Файл выслан')
        bot.send_document(chat_id=call.message.chat.id, document=open('phone_book/list.txt', 'r'))
        m_menu()
        bot.send_message(chat_id=call.message.chat.id, text="Выбери нужный пункт", reply_markup=m_menu())


def phone_add(msg):
    rl.add_log(msg.text)
    bot.send_message(chat_id=msg.from_user.id, text='Данные добавлены в книгу')
    rl.add_log('Данные добавлены в книгу')
    bk.add_contact(msg.text)
    m_menu()
    bot.send_message(msg.from_user.id, text="Выбери нужный пункт", reply_markup=m_menu())


@bot.message_handler(content_types=['document'])
def file_download(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))

    with open(filename, 'r') as file, open('phone_book/list.txt', 'a+', encoding='UTF-8') as new_book:
        new_book.write('\n')
        for line in file:
            # write content to second file
            new_book.write(line)
    # shutil.copyfile(filename, 'phone_book/list.txt')
    os.remove(filename)
    bot.send_message(chat_id=msg.from_user.id, text='Данные добавлены в книгу')
    rl.add_log('Данные добавлены в книгу')
    m_menu()
    bot.send_message(msg.from_user.id, text="Выбери нужный пункт", reply_markup=m_menu())


def calculator(msg):
    if msg.text == "Меню":
        m_menu()
        bot.send_message(msg.from_user.id, text="Выбери нужный пункт", reply_markup=m_menu())
    else:
        res = calc.math_action(msg.text)
        rl.add_log(res)
        bot.send_message(chat_id=msg.from_user.id, text=res)
        bot.send_message(chat_id=msg.from_user.id, text='Чтобы продолжить, введите следующее выражение. Чтобы '
                                                        'вернуться, напишите "Меню"')
        bot.register_next_step_handler(msg, calculator)


def calculator_clx(msg):
    rl.add_log(msg.text)
    bot.send_message(chat_id=msg.from_user.id, text='Введите первое комплексное число в формате "2 + 3j"')
    rl.add_log('Введите первое комплексное число')
    calc.math_action_1(msg.text)
    bot.register_next_step_handler(msg, calculator_clx_1)


def calculator_clx_1(msg):
    rl.add_log(msg.text)
    bot.send_message(chat_id=msg.from_user.id, text='Введите второе комплексное число в формате "2 + 3j"')
    rl.add_log('Введите второе комплексное число')
    calc.math_action_2(msg.text)
    bot.register_next_step_handler(msg, calculator_clx_2)


def calculator_clx_2(msg):
    rl.add_log(msg.text)
    res_clx = calc.math_action_3(msg.text)
    bot.send_message(chat_id=msg.from_user.id, text=res_clx)
    rl.add_log(res_clx)
    m_menu()
    bot.send_message(msg.from_user.id, text="Выбери нужный пункт", reply_markup=m_menu())


def run_game(msg):
    rl.add_log(msg.text)
    bot.send_message(chat_id=msg.from_user.id, text=emojis.encode(game_1.field_drawing(msg.text)))
    bot.send_message(chat_id=msg.from_user.id, text='Введите позицию, '
                                                    'на которую хотите сделать ход (от 1 до 9):')
    rl.add_log('Введите позицию, на которую хотите сделать ход (от 1 до 9):')
    res = game_1.game_x_o()
    if res == 'next':
        bot.register_next_step_handler(msg, run_game)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=emojis.encode(res))
        m_menu()
        bot.send_message(msg.from_user.id, text="Выбери нужный пункт", reply_markup=m_menu())


bot.polling()
