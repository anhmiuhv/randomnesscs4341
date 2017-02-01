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

#Testing for genetics
if args.optimization == "ga":
    n = method.genetics(test, size = 100, elite = 0.2, mutation=0.5, ti=args.time)
    print(n.toList())
    print(n.sc)
    print(test.sc)

# Testing for hill climbing
# n = method.hillclimbing(test, 10)
# print(n.toList())
# print(n.score())

# Testing for annealing climbing
if args.optimization == "annealing":
    n = method.annealing(test, args.time, 100)
    print(n.toList())
    print(n.score())
    print(test.score())
    
if args.optimization == "hill":
    n = method.hillclimbing(test, args.time)
    print(n.toList())
    print(n.score())
    print(test.score())




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

