#!/usr/bin/python
# -*- coding: utf-8 -*

import os
import sys
import re

import hPModule
data = re.split('\||\t', sys.stdin.readline().strip())
Keyset = {
    'key': data[0],
    'keyvaule': data[1],
    'uidset': set()
}

data[2] = data[2].split()
for i in data[2]:
    Keyset['uidset'].add(str(i))

for line in sys.stdin:
    data = re.split('\||\t', line)
    data[2] = data[2].split()
    if Keyset['keyvaule'] != data[1]:
        print "%s|%s\t%s" % (Keyset['key'], Keyset['keyvaule'], len(Keyset['uidset']))
        Keyset['key'] = data[0]
        Keyset['keyvaule'] = data[1]
        for i in data[2]:
            Keyset['uidset'].add(str(i))
    else:
        for i in data[2]:
            Keyset['uidset'].add(str(i))
