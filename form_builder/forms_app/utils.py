import string
import random

#to get the random string
def generate_random_code(N=7):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return res
