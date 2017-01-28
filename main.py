#!/usr/bin/env python3
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