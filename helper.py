from math import sqrt
import random

prime = {9: False, 8: False, 7: True, 6: False, 5: True, 4: False, 3:True, 2:True}
def decision(probability):
    return random.random() < probability

def isPrime(num):
    ret = True
    if num == 0 or num == 1 or num < 0:
        return False
#     for i in range(2, int(sqrt(num)) + 1):
#         if num % i == 0:
#             return False
    return prime[num]

neginf = -1000000 # negative infinity
inf = 1000000   # positive infinity