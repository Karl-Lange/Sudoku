from sudoku import generate_sudoku
import sys

#konsoleninput für schwierigkeit
b = int(sys.argv[1])

#erstellen eines leeren Sudokus
sudoku = [[0 for x in range(9)] for y in range(9)]

#generieren und damit auch print des generierten Sudokus
generate_sudoku(sudoku,b)

#sample output mit 15 leeren Feldern
"""
7 3 9 4 1 5 8 2 6
5 4 6 2 3 8 7 1 9
8 2 1 9 0 7 4 3 5
6 9 0 8 2 3 1 0 4
0 8 4 7 9 1 5 6 2
2 1 7 0 5 0 3 9 0
4 5 2 3 7 9 6 0 1
1 0 3 5 8 2 9 4 7
9 7 0 0 0 6 0 5 0
"""