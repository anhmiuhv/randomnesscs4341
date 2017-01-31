#!/usr/bin/env python3
import state
import method
import argparse


#parsing option from users
parser = argparse.ArgumentParser(description='we trust in probability')
parser.add_argument('optimization',choices=['hill','annealing', 'ga'], help='The type of optimization to use:')
parser.add_argument('filename', help='the list to take in')
parser.add_argument('time', type=float, help='the time for program to run')
args = parser.parse_args()

#read the file and turn into array
f = open(args.filename)
l = [] #list of numbers

for line in f.readlines():
    cols = line.split()
    l.extend(cols)

f.close()

test = state.State(l=l)
method.genetics(test, size = 2, elite = 0.4, mutation=0.4, ti=args.time)
print(test.bin1)
print(test.bin2)
print(test.bin3)
print(test.isLegal())
print(test.score())
for i in range(1,20):
    test = test.newState()
    print(test.bin1)
    print(test.bin2)
    print(test.bin3)
    print(test.isLegal())
    print(test.score())

