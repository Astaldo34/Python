import random


def create_list(items=10, max=100):
    random_list = []
    for i in range(items):
        random_list.append(random.randint(1, max))
    return random_list
