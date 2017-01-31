from random import randint
from random import shuffle
from math import ceil
from helper import isPrime

class State:
    def __init__(self, bin1 = [], bin2 = [], bin3 = [], l = []):
        self.bin1 = list(bin1)
        self.bin2 = list(bin2)
        self.bin3 = list(bin3)
        self.dic = {}
        if (not bin1):
            temp_l = list(l)
            for i in range(0,len(temp_l)):
                if i % 3 == 0:
                    self.bin1.append(int(temp_l[i]))
                elif i % 3 == 1:
                    self.bin2.append(int(temp_l[i]))
                else:
                    self.bin3.append(int(temp_l[i]))
        for i in range(-9, 10):
            self.dic[i] = 0
        for i in self.bin1:
            self.dic[i] += 1
        for i in self.bin2:
            self.dic[i] += 1
        for i in self.bin3:
            self.dic[i] += 1
        self.length = len(self.bin1) * 3
    
    def setscore(self):
        self.sc = self.score()

    def score(self):
        score1 = 0
        score2 = 0
        score3 = 0
        sign = 1
        for num in self.bin1:
            score1 = score1 + num*sign
            sign = sign*-1
        for i in range(0, len(self.bin2) - 1):
            if self.bin2[i+1] > self.bin2[i]:
                score2 = score2 + 3
            elif self.bin2[i+1] == self.bin2[i]:
                score2 = score2 + 5
            else:
                score2 = score2 - 10
        for i in range(0, int(len(self.bin3)/2)):
            if self.bin3[i] < 0:
                score3 = score3 - 2
            elif isPrime(self.bin3[i]):
                score3 = score3 + 4
            else:
                score3 = score3 - self.bin3[i]
        for i in range(int(ceil(len(self.bin3)/2)), len(self.bin3)):
            if self.bin3[i] < 0:
                score3 = score3 + 2
            elif isPrime(self.bin3[i]):
                score3 = score3 - 4
            else:
                score3 = score3 + self.bin3[i]
        return score1 + score2 + score3

    def isLegal(self):
        if (len(self.bin1) == len(self.bin2)) and (len(self.bin1) == len(self.bin3)) and (len(self.bin3) == len(self.bin2)):
            return True
        return False

    def __eq__(self, other):
        if (len(self.bin1) == len(other.bin1)) and (len(self.bin2) == len(other.bin2)) and (len(self.bin3) == len(other.bin3)):
            return other.dic == self.dic
        return False
    
    def toList(self):
        return self.bin1 + self.bin2 + self.bin3
    
    def newState(self):
        one = randint(1,3)
        two = randint(1,3)
        bin1 = list(self.bin1)
        bin2 = list(self.bin2)
        bin3 = list(self.bin3)
        if one == 1:
            binone = bin1
        elif one == 2:
            binone = bin2
        else:
            binone = bin3
        if two == 1:
            bintwo = bin1
        elif two == 2:
            bintwo = bin2
        else:
            bintwo = bin3
        i, j = randint(0, len(bin1) - 2), randint(0, len(bin1) - 1)
        if i == j:
            i+=1
        else:
            i,j = j,i
        temp = binone[i]
        binone[i] = bintwo[j]
        bintwo[j] = temp
        return State(bin1, bin2, bin3)
