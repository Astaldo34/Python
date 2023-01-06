from datetime import datetime


def add_log(msg):
    with open('log.txt', 'a+', encoding='UTF-8') as log:
        log.write(f'{datetime.now().date()}; {datetime.now().strftime("%H:%M:%S")} - {msg}\n')
