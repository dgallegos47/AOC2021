# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:10:29 2021

@author: domin
"""

with open('day_2_test.txt') as fh:
    instructions = fh.readlines()
    
lines = [x.strip('\n') for x in instructions]

horizontal = 0
vertical = 0
aim = 0

for line in lines:
    if len(line) == 9:
        horizontal += int(line.strip('\n')[-1])
        vertical += aim * int(line.strip('\n')[-1])
    elif len(line) == 6:
        aim += int(line.strip('\n')[-1])
    elif len(line) == 4:
        aim -= int(line.strip('\n')[-1])
        
print(horizontal * vertical)
            
    