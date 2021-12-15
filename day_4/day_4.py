# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 19:46:43 2021

@author: domin
"""

class Board:
    def __init__(self, board):
        self.board = board
        
        row = []
        for i in range(len(board)):
            row.append(int(x) for x in board[i].split(' '))
            
        self.rows = row

def build_board(first, last, board_values):
    board = []
    for i in range(first, last):
        board.append(board_values[i])
        
        
    return board

with open('day_4_test.txt') as fh:
    file_lines = fh.readlines()
lines = [x.strip('\n') for x in file_lines]
    
draw_order = [int(x) for x in file_lines[0].split(',')]

board_ranges = list(range(2, len(file_lines), 6))

board_list = []

for i in range(len(board_ranges)):
    board_list.append(build_board(board_ranges[i], board_ranges[i] + 5, lines))
    
b1 = Board(board_list[1])

    

    

    

    