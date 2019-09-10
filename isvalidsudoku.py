###CHECK IF THE BOARD GIVEN IS A VALID SUDOKU BOARD OR NOT

import os
import sys
import numpy as np

def isValidSudoku(board):
        length = len(board)
        var_list = [];
        ###CHECKING ROWS OF A SUDOKU
        for i in range(length):
            var = 0
            seen = set()
            for j in range(length):
                if board[i][j] != ".":
                    if board[i][j] not in seen:
                        seen.add(board[i][j])
                    else:
                        var = var + 1
                        print(i,j,var)
                else:
                    continue
            var_list.append(var)
        print(var_list)
        return(var_list)

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
row_board = board
col_board = list(map(list, np.transpose(board)))
row_list = []
col_list = []
final_list = []
not_zero = 0

##CHECKING THE ROWS TO FIND REPEATED NUMBERS
row_list = isValidSudoku(row_board)

##CHECKING THE COLUMNS TO FIND REPEATED NUMBERS
col_list = isValidSudoku(col_board)
final_list = row_list + col_list

for items in final_list:
        if items != 0:
                not_zero = not_zero + 1
        else:
                continue
if not_zero == 0:
        print("True")
else:
        print("False")
