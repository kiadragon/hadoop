#!/usr/bin/env python
# -*- coding: utf-8 -*
import sys
from itertools import *
from operator import itemgetter
def read_file(filename):
	f = file(filename)
	for line in f:
		lines = line.strip()
		yield lines.split()
# input comes from STDIN (standard input)
def main():
    container = []
    if len(sys.argv) < 2:
	print 'You didnt input a file to read. --formal commend: $:python map.py [filename]'
	sys.exit() 
    data = read_file(sys.argv[1])
    C = [[2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [2, 3, 5], [2, 3, 5, 6], [2, 3, 5, 6, 7], [2, 5], [2, 5, 6], [2, 5, 6, 7], [5], [5, 6], [5, 6, 7]]
    for e in data:
        for R in C:
            k = [e[i] for i in R]
            print "%s|%s\t%s" % (' '.join([str(i) for i in R]), ' '.join(k), str(e[1]))

#在你写的这段程序中如果以主程序运行的话　__name__ 参数就等于 __main__ 

#有的时候写的类。模块，库，都有这段代码，如果单独运行的话，可以进行个简单的测试。如果是其他程序IMPORT的话，就不会运行 *(cite)
if __name__ == "__main__":
    main()
