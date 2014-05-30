#!/usr/bin/python
# -*- coding: utf-8 -*

import sys
import os
import re
import hPModule

def MapperPostprocess():
    for line in sys.stdin:
        line = line.strip()
        data = re.split('\||\t', line)
        print "%s|%s\t%s" % (data[0], data[1], data[2])

if __name__ == "__main__":
    MapperPostprocess()
