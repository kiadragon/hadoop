#!/usr/bin/python
# -*- coding: utf-8 -*

import random
import os
import math
import sys

import hPModule

lineNumber = hPModule.count_line()
partition = hPModule.partition


m = lineNumber / partition

def Map_Estimate_Main():
    countlines = 0
    for line in sys.stdin:
        data = line.strip().split()
        if random.random() <= p:
            for eachBatch in hPModule.BATCH:
                mapperOutput = [data[i] for i in eachBatch[0]]
                print "%s|%s\t%s" % (' '.join(str(i) for i in eachBatch[0]), ' '.join(mapperOutput), str(data[1]))
                countlines += 1
    print ' ' + str(countlines)

try:
    p = math.log(lineNumber * partition) / m
except:
    print "end!"
else:
    if __name__ == "__main__":
        Map_Estimate_Main()
