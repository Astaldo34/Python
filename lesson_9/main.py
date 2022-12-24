from telebot import TeleBot, types
import emojis

import game_1
# import phone_book.book
# import record_log
# import calc

TOKEN = ''

bot = TeleBot(TOKEN)


# # Функция для сохранения документа, отправленного боту
# @bot.message_handler(content_types=['document'])
# def answer(msg: types.Message):
#     filename = msg.document.file_name
#     with open(filename, 'wb') as file:
#         file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
#     bot.send_message(chat_id=msg.from_user.id, text='Вывожу логыыыы')
#
#     # Можете раскомментировать, если потребуется затем удалять файл после обработки,
#     # чтобы не тратить память.
#     # Не забудьте импортировать os
#     # os.remove(filename)


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
    lst = ['+', '-']
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
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "game_1":
        bot.send_message(chat_id=call.message.chat.id, text='Запускаю игру...')
        bot.send_message(chat_id=call.message.chat.id, text=emojis.encode(game_1.field_drawing()))
        bot.send_message(chat_id=call.message.chat.id, text='Введите позицию, '
                                                            'на которую хотите сделать ход (от 1 до 9):')
        bot.register_next_step_handler(call.message, run_game)
    elif call.data == "calc":
        bot.send_message(call.message.chat.id, 'Пока ещё в работе...')
    elif call.data == "phone":
        bot.send_message(call.message.chat.id, 'Пока ещё в работе...')


def run_game(msg):
    bot.send_message(chat_id=msg.from_user.id, text=emojis.encode(game_1.field_drawing(msg.text)))
    bot.send_message(chat_id=msg.from_user.id, text='Введите позицию, '
                                                    'на которую хотите сделать ход (от 1 до 9):')
    res = game_1.game_x_o()
    if res == 'next':
        bot.register_next_step_handler(msg, run_game)
    else:
        bot.send_message(chat_id=msg.from_user.id, text=emojis.encode(res))
        m_menu()
        # answer(msg)
        # bot.edit_message_text(chat_id=msg.from_user.id, text='вы вернулись в главное меню', reply_markup=mainmenu())
        bot.send_message(msg.from_user.id, text="Выбери нужный пункт", reply_markup=m_menu())


# @bot.message_handler()
# def answer(msg: types.Message):
#     text = msg.text
#     if text == '+':
#         bot.register_next_step_handler(msg, answer1)
#         bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
#     elif text == '-':
#         bot.register_next_step_handler(msg, answer2)
#         bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
#     else:
#         bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
#                                                         ', а должны были арифметическое действие')


def answer1(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


def answer2(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


bot.polling()
