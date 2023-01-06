def add_contact(msg):
    with open('phone_book/list.txt', 'a+', encoding='UTF-8') as bk:
        bk.write(f'\n{msg}')
