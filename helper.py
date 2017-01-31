from math import sqrt
import random

def decision(probability):
    return random.random() < probability

def isPrime(num):
    ret = True
    if num == 0 or num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return ret

neginf = -1000000 # negative infinity
inf = 1000000   # positive infinity