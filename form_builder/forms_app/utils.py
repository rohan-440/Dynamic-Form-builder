import string
import random


def generate_random_code(N=7):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res
