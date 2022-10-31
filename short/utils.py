from random import *
from string import ascii_letters, digits
from uuid import uuid4

from hashids import Hashids


def shorting_url(id):
    hashids = Hashids(salt='this is my salt', min_length=6)
    return hashids.encode(id)


def uuid_short():
    s = str(uuid4())
    return s[:6]


def random_choice():
    rand_str = choice(ascii_letters) + choice(digits) + choice(ascii_letters) + choice(digits) + choice(
        ascii_letters) + choice(digits)
    return rand_str


print(uuid_short())
print(random_choice())
print(shorting_url(10))
