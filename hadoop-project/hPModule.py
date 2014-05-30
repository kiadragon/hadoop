#!/usr/bin/python
# -*- coding: utf-8 -*

#hPModule Hadoop-Project-Module python file
import sys
import os
#define your file line number
lineNumber = 10000 # changeable

BATCH = [[[2, 3, 4, 5, 6, 7],[2, 3, 4, 5, 6],[2, 3, 4, 5], [2, 3, 4], [2, 3], [2]],
         [[2, 3, 5, 6, 7], [2, 3, 5, 6], [2, 3, 5]],
         [[2, 5, 6, 7], [2, 5, 6], [2, 5]],
         [[5, 6, 7], [5, 6], [5]]]

partition = 10

def count_line():
    return int(lineNumber)



