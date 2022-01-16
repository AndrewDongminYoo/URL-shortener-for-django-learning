import string
import random

# Create your models here.


def rand_letter():
    return random.choice(string.ascii_letters).lower()


def rand_string():
    return "".join([random.choice(string.digits + string.ascii_letters) for _ in range(6)])
