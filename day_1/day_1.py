# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:34:39 2021

@author: dgallegos
"""

filename = 'day_1.txt'

with open(filename) as fh:
    data = [int(x) for x in fh]
 
lower_center = 1
upper_center = 2

increase_count = 0

for i in range(len(data) - 3):
    lower_sum = data[lower_center- 1] + data[lower_center] + data[lower_center + 1]
    upper_sum = data[upper_center- 1] + data[upper_center] + data[upper_center + 1]
    
    if upper_sum > lower_sum:
        increase_count += 1
        
    lower_center += 1
    upper_center += 1
    
    
