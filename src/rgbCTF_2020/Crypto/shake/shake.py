# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 01:58:22 2020

@author: cruffo
"""

line_col = [[33, 20],[71, 5],[43, 142],[60, 150],[73, 312],[78, 66],[15, 22],
            [12, 115],[29, 18],[51, 147],[45, 68],[34, 14],[54, 126],[15, 48],
            [3, 4],[60, 126],[45, 77],[13, 69]]


play = 'play'

fh = open(play, 'r')
lines = fh.readlines();

for item in line_col:
    print(lines[item[0]][item[1]],end='')
    