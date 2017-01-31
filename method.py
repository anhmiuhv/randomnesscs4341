import state
import random
import helper
from random import randint
import time

def genetics(test, size, elite, mutation,ti):
    popu = [test]
    for i in range(100 - 1):
        popu.append(test.newState())
    maximum = helper.neginf
    mininum = helper.inf
    for i in popu:
        i.setscore()
        
    popu.sort(key=lambda x: x.sc)
    
    def random_selection():
        length = len(popu)
        choosen = length * (1 - elite)
        c1 = randint(int(choosen), length - 1)
        return popu[c1]
        
            
    t = time.time()    
    while(time.time() - t < ti):
        new_population = []
        for i in range(size):
            x = random_selection()
            y = random_selection()
            #child = reproduce(x, y)
            

    return 1
