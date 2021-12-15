# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 19:08:17 2021

@author: domin
"""


def most_common(values, pos, case):
    one_count = 0
    zero_count = 0    
    for value in values:
        if value[pos] == '1':
            one_count += 1
        else:
            zero_count += 1
    
    if zero_count > one_count:
        common_bit = '0'
    elif one_count > zero_count:
        common_bit = '1'
    elif zero_count == one_count:
        if case == 'ox':
            common_bit = '1'
        else:
            common_bit = '0'
    
    return common_bit


with open('day_3.txt') as fh:
    file_lines = fh.readlines()
    
lines = [x.strip('\n') for x in file_lines]

gamma_rate = ''

for i in range(len(lines[0])):
    one_count = 0
    zero_count = 0
    
    for item in lines:
        if item[i] == '0':
            zero_count += 1
        else:
            one_count += 1
    
    if zero_count > one_count:
        gamma_rate = gamma_rate + '0'
    else:
        gamma_rate = gamma_rate + '1'
          
epsilon_rate = ''

for bit in gamma_rate:
    if bit == '1':
        epsilon_rate = epsilon_rate + '0'
    else:
        epsilon_rate = epsilon_rate + '1'
        
print(int(epsilon_rate, 2) * int(gamma_rate, 2))

with open('day_3.txt') as fh:
    file_lines = fh.readlines()
    
lines = [x.strip('\n') for x in file_lines]

values = lines

for i in range(len(values[0])):
    common_bit = most_common(values, i, 'ox')
    
    new_values = []
    
    for entry in values:
        if entry[i] == common_bit:
            new_values.append(entry)
            
    values = new_values
    if len(values) == 1:
        break

ox_rate = int(values[0], 2)

values = lines

for i in range(len(values[0])):
    common_bit = most_common(values, i, 'ox')
    
    new_values = []
    
    for entry in values:
        if entry[i] != common_bit:
            new_values.append(entry)
            
    values = new_values
    if len(values) == 1:
        break
    
co2_rate = int(values[0], 2)

print(co2_rate * ox_rate)



        