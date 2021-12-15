# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:50:54 2021

@author: domin
"""

with open('day_5_test.txt') as fh:
    file_data = fh.readlines()
    
x1y1_list = []
x2y2_list = []
    
for line in file_data:
    line_string = line.replace('\n','')
    
    x1y1_list.append([int(x) for x in line_string.split(' -> ')[0].split(',')])
    x2y2_list.append([int(x) for x in line_string.split(' -> ')[1].split(',')])

# pt_list = [[x1_list[i], y1_list[i], x2_list[i], y2_list[i]] for i in range(len(x1))] 
  
x1_list = [x[0] for x in x1y1_list]
y1_list = [x[1] for x in x1y1_list]

x2_list = [x[0] for x in x2y2_list]
y2_list = [x[1] for x in x2y2_list]

minx = min([min(x1_list), min(x2_list)])
miny = min([min(y1_list), min(y2_list)])

maxx = max([max(x1_list), max(x2_list)]) + 1
maxy = max([max(y1_list), max(y2_list)]) + 1

maxmax = max([minx, miny, maxx, maxy])
matrix = [ [ 0 for i in range(0, maxmax) ] for j in range(0, maxmax) ]
    
for k in range(len(x1_list)):
    # print(k)
    x1 = x1_list[k]
    y1 = y1_list[k]
    x2 = x2_list[k]
    y2 = y2_list[k]  
    # print(f'({x1}, {y1}) -> ({x2}, {y2})')
    
    if x1 > x2:
        x2 = x1
        x1 = x2_list[k]
        
    if y1 > y2:
        y2 = y1
        y1 = y2_list[k]
    
    if y1 == y2:
        for i in range(x1, x2+1):
            matrix[y1][i] += 1
            # print(f' Horizontal ({y1}, {i})')
    elif x1 == x2:
        for j in range(y1, y2+1):
            matrix[j][x1] += 1  
            # print(f'Vertical ({j}, {x1})')
    elif (x2-x1) == (y2-y1):
        steps = x2 - x1
        for i in range(steps):
            matrix[y1 + i][x1 + i] += 1
            # print(f'k: {k}, ({x1+i}, {y1+i})')
            

                
counts = [item for sublist in matrix for item in sublist]
a = list(filter((1).__ne__, counts))
b = list(filter((0).__ne__, a))
print(len(b))

        
    