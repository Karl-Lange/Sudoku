#Solver
import random
import sys


#funktion zum auslesen eines dusokus aus einer csv datei
def read_csv(filename):
    with open(filename) as f:
        #erstellen der finalen Liste
        sudoku = []
        #zusammenführen der einzelnen Listen in eine große Nested Liste in finaler später verwendeten Form
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split(';')]
            sudoku.append(inner_list)
        return sudoku


#Funktion zum finden des nächsten leeren Feldes (also ein Feld mit Inhalt 0) und return des Feldes
def find_empty_square(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return(i,j)
    return None

#Funktion zum checken, ob eine eingesetzte Zahl als Valid eingestuft wird, also unique in Zeile, Spalte und jeweiligem 3x3 Quadrat ist
def valid(sudoku, num, pos):
    size = 9
    #hier wird gecheckt, ob die Reihe gültig ist
    for i in range(size):
        #check, dass wir nicht an der selben Stelle auf die selbe Zahl testen
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False
    #hier wird gecheckt, ob die Spalte gültig ist
    for i in range(size):
        # check, dass wir nicht an der selben Stelle auf die selbe Zahl testen
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False
    #hier wird gecheckt, ob das 3x3 Raster gültig ist
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sudoku[i][j] == num and (i, j) != pos:
                return False

    return True

#Funktion, welche ein vorgegebenes Sudoku löst
def solve(sudoku):
    num_list = [1,2,3,4,5,6,7,8,9]
    #erzeugung einer zufääligen Liste aus num_list, um verschiedene Sudokus zu erzeugen und nicht immer das selbe
    random.shuffle(num_list)
    #Zuweisen des nächsten leeren Feldes
    find = find_empty_square(sudoku)
    #wenn kein leeres Feld gefunden wird, ist das Sudoku gelöst
    if not find:
        return True
    #Wenn ein Feld gefunden wird, werden reihe und Spalte zugewiesen
    else:
        row, col = find
    #Jetzt wird jede zulässige Zahl (1-9) ausprobiert und durch die Funktion valid gecheckt
    #for i in random.shuffle(list(range(1,10))):
    for i in num_list:
        if valid(sudoku, i, (row, col)):
            #Wenn Valid True ist, wird dem Feld die Zahl i zugewiesen
            sudoku[row][col] = i
            #hier wird die Funktion solve revursive aufgerufen, bis das Sudoku gelöst wird, falls keine Lösung möglich ist,
            #wird der letzten betrachteten Stelle eine 0 und der Prozess wiederholt sich
            if solve(sudoku):
                #return True
                return True
            sudoku[row][col] = 0

#Funktion, um die Nested List in einer lesbareren Form zu printen
def print_sudoku(sudoku):
    for item in sudoku:
        print(' '.join(str(x) for x in item))

#Funktion, um ein Zufälliges Feld in einem Sudoku zu wählen
def random_field():
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    return row, col

#Funktion zum check, ob für ein leeres Feld im Sudoku eine eindeutige Lösung gefunden wird
def check_eindeutigkeit(col, row, sudoku):
    list_valid = []
    for i in range(1, 9):
        if valid(sudoku, i, (row, col)):
            list_valid.append(i)
    return len(list_valid) == 1

#Funktion zum Erzeugen eines neuen Sudokus mit input von einem leeren sudoku in nested list form und einem Parameter b,
#welcher die Anzahl der leeren Felder (also im Endeffekt Schwirigkeit) angibt
def generate_sudoku(sudoku, b):
    #ein leeres Sudoku lösen und damit ein zufälliges neues Sudoku erschaffen
    solve(sudoku)
    list_felder = []
    counter_zurückgesetzt = 0
    felder_zurückgesetzt = 0
    while counter_zurückgesetzt < 10:
        #random eine Zahl aus dem Sudoku löschen
        row, col = random_field()
        feld = row*col
        #check, ob das gelöscht Feld schon einmal gelöscht wurde
        if feld not in list_felder:
            list_felder.append(feld)
            old_number = sudoku[row][col]
            sudoku[row][col] = 0
            #Ausprobieren, welche Zahlen in das gelöschte Feld passen, wenn nicht zurücksetzen des Feldes auf ursprünglichen Wert
            is_eindeutig = check_eindeutigkeit(col, row, sudoku)
            if is_eindeutig:
                counter_zurückgesetzt = 0
                felder_zurückgesetzt += 1
            else:
                counter_zurückgesetzt += 1
                sudoku[row][col] = old_number
        #Abbruchkriterium wenn gewünschte leere Feldanzahl erreicht wird
        if felder_zurückgesetzt >= b-1:
            break
    #print des generierten Sudokus mit Leerfeldern
    print_sudoku(sudoku)

