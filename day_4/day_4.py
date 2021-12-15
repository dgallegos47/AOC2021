# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:30:13 2021

@author: dgallegos
"""

class Board():
    def __init__(self, board):
        self.rows = []
        self.cols = []
        for i in range(5):
            self.rows.append(board[i])
            col = []
            for j in range(5):
                col.append(board[j][i])
            self.cols.append(col)
        
        self.numbers = [item for row in self.rows for item in row]
            
    def bingo_check(self, number_list):
        row_bingo = False
        col_bingo = False
        for row in self.rows:
            row_bingo = row_bingo or all(number in number_list for number in row)
        for col in self.cols:
            col_bingo = col_bingo or all(number in number_list for number in col)
            
        return row_bingo or col_bingo
    
    def board_score(self, number_list):
        last_number = number_list[-1]
        unmarked_numbers = [x for x in self.numbers if x not in number_list]

        return sum(unmarked_numbers)*last_number
        
            
with open('day_4.txt') as fh:
    data = fh.readlines()
    
number_list = [int(x) for x in str(data[0].replace('\n', '')).split(',')]

empty_row = list(range(1, len(data), 6))

boards = []

for i in range(len(empty_row)):
    sub_list = []
    for j in range(1,6):
        # sub_list.append(data[empty_row[i] + j].replace('\n',''))
        line = data[empty_row[i] + j].replace('\n', '').split(' ')
        trimmed_line = list(filter(''.__ne__, line))
        sub_list.append([int(x) for x in trimmed_line])
        # sub_list.append([int(x) for x in data[empty_row[i] + j].replace('\n', '').split(' ')])
    
    boards.append(Board(sub_list))
    
bingo = False
i = 0
call_list = []
call_list.append(number_list[0])

bingo_scores = []
last_removed_score = 0

while bingo == False:
    for board in boards:
        if board.bingo_check(call_list) == True:
            bingo_scores.append(board.board_score(call_list))
            boards.remove(board)
            # bingo = True
    
    if i != len(number_list) - 1:
        i += 1
        call_list.append(number_list[i])
    else:
        bingo = True

    
    
    


