import numpy as np
import platform, subprocess

def turn(player):
    while True:
        koordinat = input("Pilih koordinat (x (spasi) y): ").split(" ")
        for i in range(len(koordinat)):
            koordinat[i] = int(koordinat[i])
        x = koordinat[0]
        y = koordinat[1]

        if board[3-y][x-1] == '*':
            board[3-y][x-1] = player
            break
        else:
            print("Pilih ulang!")
            continue

def print_board():
    for i in range(n):
        print(n-i, end="  ")
        for j in range(n):
            print(board[i][j], end=" ")

        print()
    print("   1 2 3")

def board_checking(x):
    # n = len(x)
    # horizontal checking
    for i in range(n):
        if x[i].__contains__("*"):
            continue
        if len(set(x[i])) == 1:
            return x[i][0]
        
    #  diagonal checking
    temp = set([x[i][i] for i in range(n)])
    if '*' not in temp and len(temp) == 1:
        return ''.join(temp)
    
    temp = set([x[i][2-i] for i in range(n)])
    if '*' not in temp and len(temp) == 1:
        return ''.join(temp)

    # vertical checking
    x = np.array(x).T.tolist()
    for i in range(n):
        if x[i].__contains__("*"):
            continue
        if len(set(x[i])) == 1:
            return x[i][0]
        
    return -1

def winner_checking():
    win = board_checking(board)
    if win != -1:
        if player1 == win:
            globals()['winner'] = "player 1"
        else:
            globals()['winner'] = "player 2"        

def clear_screen():
    if platform.system() == "windows":
        if platform.release() in {10, 11}:
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    # linux and mac
    else:
        print("\033c", end="")

winner = 0
board = [
    ["*", '*', '*'],
    ["*", '*', '*'],
    ["*", '*', '*']
]
print("Welcome to deadly tic tac toe game!")
symbol = input("Pilih X atau O: ").upper()
n = len(board)

while True:
    if symbol == "X":
        player1 = "x"
        player2 = "O"
        break
    elif symbol == "O":
        player2 = "x"
        player1 = "O"
        break
    else:
        print("Pilih X atau O")

clear_screen()
game_over = False
turn_phase = 0

while not game_over:
    print_board()
    turn_phase += 1
    # jika turn phase ganjil maka player 1 jalan
    if turn_phase % 2 != 0:
        print("Player 1 jalan: ")
        turn(player1)
    else:
        print("Player 2 jalan: ")
        turn(player2)
    clear_screen()
    winner_checking()
    if winner != 0 or '*' not in [board[x][j] for x in range(n) for j in range(n)]:
        game_over = True

print_board()
if winner != 0:
    print(f"Pemenangnya adalah {winner}")
else:
    print('tidak ada yang menang!')
