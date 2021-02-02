import random


def random_hex_color():
    r = hex(random.randint(16, 255))[2:]
    g = hex(random.randint(16, 255))[2:]
    b = hex(random.randint(16, 255))[2:]
    return r, g, b


def move_top_left(tur):
    tur.setposition(-200, 200)
    tur.clear()