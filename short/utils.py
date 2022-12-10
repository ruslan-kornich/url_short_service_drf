from random import *
from string import ascii_letters, digits


def random_choice():
    rand_str = choice(ascii_letters) + choice(digits) + choice(ascii_letters) + choice(digits) + choice(
        ascii_letters) + choice(digits)
    return rand_str
