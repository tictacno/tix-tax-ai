import numpy as np
import board, game

#Defines if move is valid or not
def valid_move(x, y):
    try:
        if board.mib[x][y] == 0 and board.mab[x] == 0:
            return True
        else:
            print('The move is invalid. Choose a new position')
            return False
    except:
        print('Position provided is not in domain.')
        return False

#(Currently) Updates micro boards once 3 pieces are connected
    ##Add support for marco as well
def update_board(x, player):
    micro = board.mib[x]
    for i in range(0,2):
        #column
        if micro[i] != 0 and micro[i] == micro[i+3] and micro[i] == micro[i+6]:
            board.mab[x] = player
            return
        #row
        if micro[(3*i)] != 0 and micro[(3*i)] == micro[(3*i)+1] and micro[(3*i)] == micro[(3*i)+2]:
            board.mab[x] = player
            return
        #diagonal
        if micro[0] != 0 and micro[0] == micro[4] and micro[0] == micro[8]:
            board.mab[x] = player
            return
        #anti-diagonal
        if micro[2] != 0 and micro[2] == micro[4] and micro[2] == micro[6]:
            board.mab[x] = player
            return

#Intented to return 0 (running), 1 (player 1 win), -1 (player 2 win), or 2 (draw)
def game_state():
    return 0
