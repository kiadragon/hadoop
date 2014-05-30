#!/usr/bin/python
# -*- coding: utf-8 -*

import os
import sys
import re

import hPModule
batch = hPModule.BATCH
partition = hPModule.partition
keygroup = {
    '2 3 4 5 6 7': { 'uidset': set() },
    '2 3 4 5 6': { 'uidset': set() },
    '2 3 4 5': { 'uidset': set() },
    '2 3 4': { 'uidset': set() },
    '2 3': { 'uidset': set() },
    '2': { 'uidset': set() },
    '2 3 5 6 7': { 'uidset': set() },
    '2 3 5 6': { 'uidset': set() },
    '2 3 5': { 'uidset': set() },
    '2 5 6 7': { 'uidset': set() },
    '2 5 6': { 'uidset': set() },
    '2 5': { 'uidset': set() },
    '5 6 7': { 'uidset': set() },
    '5 6': { 'uidset': set() },
    '5': { 'uidset': set() }
}


# GET firstline data to init keygroup




# init keygroup 
def initSet(keygroup, data):
    keygroup[data[1]]['keyvaule'] = data[2]
    keygroup[data[1]]['uidset'].add(int(data[3]))


count = 0
for eachline in sys.stdin:
    eachline = eachline.strip()
    data = re.split(',|\||\t', eachline) # divide data
    data[2] = data[2].split()
    #judge data[1] length to decide how many time to substract
    
    if len(data[2]) == 6:
        count = 6
    else:
        count = 3
        
    while count != 0:
        if keygroup[data[1]]['uidset'] == set([]):
            initSet(keygroup, data)
        
        
        if keygroup[data[1]]['keyvaule'] != data[2]:
            print "%s|%s\t%s" % (data[1], ' '.join(str(i) for i in keygroup[data[1]]['keyvaule']),
                                     ' '.join(str(i) for i in keygroup[data[1]].pop('uidset')))
            keygroup[data[1]]['keyvaule'] = data[2]
            keygroup[data[1]]['uidset'] = set()
            keygroup[data[1]]['uidset'].add(int(data[3]))
            
        else:
            keygroup[data[1]]['uidset'].add(int(data[3]))
            
        data[1] = data[1][0:len(data[1]) - 2]
        data[2] = data[2][0:len(data[2]) - 1]
        count -= 1

    
