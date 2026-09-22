# Programme for tic tac toe

import random

print("1:O", "2:X")

while True:
    a = int(input("Enter your choice between 1 and 2: "))

    if a == 1:
        player = 'O'
        computer = 'X'
        break

    elif a == 2:
        player = 'X'
        computer = 'O'
        break

    else:
        print("Please enter a valid choice")


c = ['1','2','3','4','5','6','7','8','9']


def board():
    print(f"_{c[0]}_|_{c[1]}_|_{c[2]}_")
    print(f"_{c[3]}_|_{c[4]}_|_{c[5]}_")
    print(f" {c[6]} | {c[7]} | {c[8]} ")


board()


def player_turn():
    while True:
        b = int(input("Enter your choice: "))

        if 1 <= b <= 9:
            if c[b-1] not in ['O','X']:
                c[b-1] = player
                break
            else:
                print("Position is already occupied!")
        else:
            print("Enter a valid position")

    board()


def computer_turn():
    available = []

    for i in range(9):
        if c[i] not in ['O','X']:
            available.append(i)

    computer_choice = random.choice(available)
    c[computer_choice] = computer

    print()
    board()


def check_win():
    w = [[0,1,2], [3,4,5], [6,7,8],
         [0,3,6], [1,4,7], [2,5,8],
         [0,4,8], [2,4,6]]

    for combination in w:
        if c[combination[0]] == c[combination[1]] == c[combination[2]]:
            return True

    return False


def check_draw():
    for i in range(9):
        if c[i] not in ['O','X']:
            return False

    return True


for x in range(9):

    player_turn()

    if check_win():
        print("CONGRATULATIONS!!, YOU WON!!🏆🎊")
        break

    if check_draw():
        print("DRAW")
        break

    computer_turn()

    if check_win():
        print("The computer won, better luck next time...")
        break

    if check_draw():
        print("DRAW")
        break