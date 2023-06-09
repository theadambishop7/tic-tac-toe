from os import system

positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
divider = "-----------"


def print_instructions():
    print("Welcome to Tic Tac Toe!\n")
    print("Use this key to select your space:\n")
    print("1 | 2 | 3")
    print(divider)
    print("4 | 5 | 6")
    print(divider)
    print("7 | 8 | 9\n")


def current_board():
    row_1 = []
    row_2 = []
    row_3 = []
    for item in positions[:3]:
        row_1.append(item)
    for item in positions[3:6]:
        row_2.append(item)
    for item in positions[6:9]:
        row_3.append(item)
    print(" | ".join(row_1))
    print(divider)
    print(" | ".join(row_2))
    print(divider)
    print(" | ".join(row_3))
    print("\n")


def check_win(player_token):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in win_conditions:
        if positions[win[0]] == player_token \
                and positions[win[1]] == player_token \
                and positions[win[2]] == player_token:
            return True
    return False


print_instructions()
while True:
    not_valid = True
    while not_valid:
        player_1 = int(input("Player 1\nWhere do you want to go?\n"))
        try:
            desired_position = positions[player_1 - 1]
        except IndexError:
            system("clear")
            current_board()
            print("Invalid Selection. Try Again.")
        else:
            if desired_position != " ":
                system("clear")
                current_board()
                print("Space already taken. Try Again")
            else:
                positions[player_1 - 1] = "X"
                not_valid = False
    if check_win("X"):
        winner = "Player 1"
        system("clear")
        break
    system("clear")
    current_board()

    not_valid = True
    while not_valid:
        player_2 = int(input("Player 2\nWhere do you want to go?\n"))
        try:
            desired_position = positions[player_2 - 1]
        except IndexError:
            system("clear")
            current_board()
            print("Invalid Selection. Try Again.")
        else:
            if desired_position != " ":
                system("clear")
                current_board()
                print("Space already taken. Try Again")
            else:
                not_valid = False
                positions[player_2 - 1] = "O"
                print(not_valid)
    if check_win("O"):
        winner = "Player 2"
        system("clear")
        break
    system("clear")
    current_board()

print(f"{winner} WINS!!!")
current_board()
