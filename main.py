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
#20 0.2
#200 0.2
#1000 0.2

#200 1 bad
#20 1 worse
#

n = method.genetics(test, size = 1000, elite = 0.5, mutation=0.5, ti=args.time)
print(n.toList())
print(n.sc)
print(test.sc)
# print(test.bin1)
# print(test.bin2)
# print(test.bin3)
# print(test.isLegal())
# print(test.score())
# for i in range(1,20):
#     test = test.newState()
#     print(test.bin1)
#     print(test.bin2)
#     print(test.bin3)
#     print(test.isLegal())
#     print(test.score())

