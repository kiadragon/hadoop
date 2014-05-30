#!/usr/bin/python
# -*- coding: utf-8 -*

import os
import sys
import linecache
import hPModule

def Reducer_Estimate_Main():
    sample_number = 0
    for line in sys.stdin:
        if line[0] == ' ':
            sample_number += int(line[1:])
        else:
            break

    partition = hPModule.partition
    
    interval = (sample_number + partition - 1) / partition
    count = 1
    
    for line in sys.stdin:
        if (count % interval) == 0 and count != sample_number:
            print str(line.strip('\n'))
        count += 1


if __name__ == "__main__":
    Reducer_Estimate_Main()
