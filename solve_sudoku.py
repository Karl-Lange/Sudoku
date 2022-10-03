from sudoku import solve, print_sudoku, read_csv
import sys

filename = str(sys.argv[1])
sudoku = read_csv(filename)

print("Anfangssudoku")
print_sudoku(sudoku)
solve(sudoku)
print("")
print("Gelöstes Sudoku")
print_sudoku(sudoku)
