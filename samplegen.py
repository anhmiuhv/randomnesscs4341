#!/usr/bin/env python3
import argparse
import math
import heapq
from random import randint

#parsing option from users
parser = argparse.ArgumentParser(description='New sample generator')
parser.add_argument('filename', help='the name of the file for terrain info')
parser.add_argument('binsize', type=int, help='size of bin')
args = parser.parse_args()

f = open(args.filename, "w")
st = ""

for i in range(0, args.binsize):
    st += str(randint(-9, 9)) + " "
    st += str(randint(-9, 9)) + " "
    st += str(randint(-9, 9)) + " "

f.write(st)
f.close()

