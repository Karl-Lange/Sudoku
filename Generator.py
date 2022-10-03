from sudoku import generate_sudoku
import sys

#konsoleninput für schwierigkeit
b = int(sys.argv[1])

#erstellen eines leeren Sudokus
sudoku = [[0 for x in range(9)] for y in range(9)]

generate_sudoku(sudoku,b)