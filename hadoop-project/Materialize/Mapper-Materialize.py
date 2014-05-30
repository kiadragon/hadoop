#!/usr/bin/python
# -*- coding: utf-8 -*

import os
import sys

import hPModule

partition = hPModule.partition
partitionfile = open('part-00000')
boundary = []
linenumber = partition - 1 # Linenumber is a constant
for i in partitionfile:
    boundary.append(i.strip('\n'))
partitionfile.close()

def mapMaterialize():
    for line in sys.stdin:
        data = line.strip().split()
        for eachBatch in hPModule.BATCH:
            batch = [data[i] for i in eachBatch[0]]
            keyvaule = ' '.join(str(i) for i in eachBatch[0]) + '|' + ' '.join(batch) # + "\t" + str(data[1])
            partitionnumber = judgeWhichPartition(boundary, keyvaule)
            print "%s,%s\t%s" % (str(partitionnumber), keyvaule, str(data[1]))

def judgeWhichPartition(boundary, key):
    start = 0
    end = partition - 1
    while start < end:
        mid = int((start + end) / 2) # binary search
        if boundary[mid] < key:
            start = mid + 1
        elif boundary[mid] > key:
            end = mid - 1
        else:
            return (mid + 1)
    return start

if __name__ == "__main__":
    mapMaterialize()
