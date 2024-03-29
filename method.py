import state
import random
import helper
from random import randint
import time
import math
dic = {}

def reproduce(x, y):
    #apply PMX accourding to wikipedia
    size = x.length
    cxpoint1 = randint(0, size)
    l1 =  x.toList()
    l2 = y.toList()
    l3 = list(l1[0:cxpoint1])
    d = dict(dic)
    for i in l3:
        d[i] -= 1
    for i in range(size):
        j = l2[i]
        if d[j] == 0:
            continue
        l3.append(j)
        d[j] -= 1

    return state.State(bin1=l3[0:size//3], bin2=l3[size//3:size//3*2], bin3=l3[size//3*2:])



def genetics(test, size, elite, mutation,ti):
    global dic
    popu = [test]
    dic = test.getdic()

    for i in range(100 - 1):
        popu.append(test.shuffle())
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
        popu = new_population
        popu.sort(key=lambda x: x.sc)


    return popu[-1]


def hillclimbing(state, ti):
    potentialSolution = []
    countSolution = 0
    countTime = 0
    currentState = state
    potentialSolution.append(currentState)
    t = time.time()
    while(time.time() - t < ti):
        currentState = potentialSolution.pop()
        nextState = currentState.newState()
        if (nextState.score() > currentState.score()):
            currentState = nextState
            countTime = 0
        else:
            countTime += 1
        potentialSolution.append(currentState)
        if (countTime == 100):
            countTime = 0
            countSolution +=1
            currentState = state.shuffle()
            potentialSolution.append(currentState)

    bestSolution = potentialSolution[0]
    for i in range(0, len(potentialSolution)):
        if (potentialSolution[i].score() > bestSolution.score()):
            bestSolution = potentialSolution[i]

    return bestSolution

def annealing(state, ti, maxtemp, scale):
    potentialSolution = []
    countSolution = 0
    countTime = 0
    countTemp = 0
    currentState = state
    state.setscore()
    potentialSolution.append(currentState)

    t =  time.time()
    while(time.time() - t < ti):
        currentState = potentialSolution.pop()
        nextState = currentState.newState()
        nextState.setscore()
        delta = (nextState.sc- currentState.sc)*scale
        temperature = (maxtemp - countTemp)
        if (delta > 0):
            currentState = nextState
            countTemp += 1
            countTime = 0
        else:
            
            
            probabilitytaken = math.exp(delta/temperature)

            if (random.random() < probabilitytaken):
                currentState = nextState
                countTemp += 1

            countTime += 1

        potentialSolution.append(currentState)
        if ((countTime == 100)or(temperature <= 1)):
            countTemp = 0
            temperature = maxtemp
            countTime = 0
            countSolution +=1
            currentState = state.shuffle()
            currentState.setscore()
            potentialSolution.append(currentState)

    bestSolution = potentialSolution[0]
    for i in range(0, len(potentialSolution)):
        if (potentialSolution[i].score() > bestSolution.score()):
            bestSolution = potentialSolution[i]

    return bestSolution

