import state
import random
import helper
from random import randint
import time
def reproduce(x, y):
    #apply PMX accourding to wikipedia
    size = x.length
    cxpoint1 = randint(1, size)
    l1 =  x.toList()
    l2 = y.toList()
    l3 = list(l1[0:cxpoint1])
    dic = dict(x.dic)
    for i in l3:
        dic[i] -= 1
    count = cxpoint1
    for i in range(size):
        j = l2[i]
        if dic[j] == 0:
            continue
        l3.append(j)
        dic[j] -= 1
    
    return state.State(bin1=l3[0:size//3], bin2=l3[size//3:size//3*2], bin3=l3[size//3*2:])
    
    
    
def genetics(test, size, elite, mutation,ti):
    popu = [test]
    for i in range(100 - 1):
        popu.append(test.newState())
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
            child = reproduce(x, y)
            if helper.decision(mutation):
                child = child.newState()
            new_population.append(child)
            child.setscore()
        popu.extend(new_population)
        popu.sort(key=lambda x: x.sc)
            

    return popu[-1]


def hillclimbing(state, maxiteration):
    potentialSolution = []
    countSolution = 0;
    countTime = 0
    currentState = state
    
    while(countSolution < maxiteration):
        nextState = currentState.newState()
        if (nextState.score() > currentState.score()):
            currentState = nextState
            countTime = 0
        else:
            countTime += 1
            
        if (countTime == 100):
            countTime = 0
            countSolution +=1
            potentialSolution.append(currentState)
            currentState = state.shuffle()
    
    bestSolution = potentialSolution[0]
    for i in range(0, len(potentialSolution)):
        if (potentialSolution[i].score() > bestSolution.score()):                
            bestSolution = potentialSolution[i]

    return bestSolution
