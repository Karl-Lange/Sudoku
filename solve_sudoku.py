from sudoku import solve, print_sudoku, read_csv
import sys

#Eingabe des Filenames, welche das Sudoku beinhaltet und einlesen der Datei
filename = str(sys.argv[1])
sudoku = read_csv(filename)

#Print von Anfangssudoku, lösen des Sudokus und print des gelösten Sudokus
print("Anfangssudoku")
print_sudoku(sudoku)
solve(sudoku)
print("")
print("Gelöstes Sudoku")
print_sudoku(sudoku)

#Sample Output mit sudoku_1.csv
"""
Anfangssudoku
7 8 0 4 0 0 1 2 0
6 0 0 0 7 5 0 0 9
0 0 0 6 0 1 0 7 8
0 0 7 0 4 0 2 6 0
0 0 1 0 5 0 9 3 0
9 0 4 0 6 0 0 0 5
0 7 0 3 0 0 0 1 2
1 2 0 0 0 7 4 0 0
0 4 9 2 0 6 0 0 7

Gelöstes Sudoku
7 8 5 4 3 9 1 2 6
6 1 2 8 7 5 3 4 9
4 9 3 6 2 1 5 7 8
8 5 7 9 4 3 2 6 1
2 6 1 7 5 8 9 3 4
9 3 4 1 6 2 7 8 5
5 7 8 3 9 4 6 1 2
1 2 6 5 8 7 4 9 3
3 4 9 2 1 6 8 5 7



"""
