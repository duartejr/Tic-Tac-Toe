import string
field = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
marks = ["X", "O"]

def print_field():
    print("-"*9)
    for line in range(3):
        str = "| "
        str += " ".join(field[line])
        str += "|"
        print(str)
    print("-"*9)


def check_winner():
    if win_line() in marks:
        return win_line()
    if win_diag() in marks:
        return win_diag()
    if win_col() in marks:
        return win_col()
    if not_finished():
        return False
    else:
        return "Draw"


def not_finished():
    for x in field:
        if "_" in x:
            return True
    return False


def win_line():
    wins = ""
    for l in range(3):
        if field[l].count("X") == 3:
            if wins != "O":
                wins = "X"
            else:
                return "Impossible"
        elif field[l].count("O") == 3:
            if wins != "X":
                wins = "O"
            else:
                return "Impossible"
    return wins


def win_diag():
    first_diag = [field[x][x] for x in range(3)]
    second_diag = [field[x][-x-1] for x in range(3)]
    wins = ""
    if first_diag.count("X") == 3 or second_diag.count("X") == 3:
        if wins != "O":
            wins = "X"
        else:
            return "Impossible"
    elif first_diag.count("O") == 3 or second_diag.count("O") == 3:
        if wins != "X":
            wins = "O"
        else:
            return "Impossible"
    return wins


def win_col():
    wins = ""
    for c in range(3):
        col = [field[x][c] for x in range(3)]
        if col.count("X") == 3:
            if wins != "O":
                wins = "X"
            else:
                return "Impossible"
        if col.count("O") == 3:
            if wins != "X":
                wins = "O"
            else:
                return "Impossible"
    return wins


def count_cells():
    countX = 0
    countY = 0
    for l in field:
        countX += l.count("X")
        countY += l.count("O")
    if abs(countX-countY) > 1:
        return "Impossible"
    return "Possible"


def update_field(coords, mark):
    status = False
    if coords[0] not in string.digits or coords[1] not in string.digits:
        print("You should enter numbers!")
    else:
        coords = [int(x) for x in coords]
        if max(coords) > 3 or min(coords) < 1:
            print("Coordinates should be from 1 to 3!")
        else:
            if field[-coords[1]][coords[0]-1] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                field[-coords[1]][coords[0]-1] = mark
                print_field()
                status = True
    return status


print_field()
mark = "X"

while check_winner() == False:
    coords = input("Enter the coordinates: ").split()
    while not update_field(coords, mark):
        coords = input("Enter the coordinates: ").split()
    if mark == "X":
        mark = "O"
    else:
        mark = "X"
    winner = check_winner()

if winner == "Draw":
    print(winner)
else:
    print(winner, "wins")
