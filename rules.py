import numpy as np
import board, game

#Defines if move is valid or not
def valid_move(x, y):
    try:
        #If the micro position is not taken and the macro is not as well
        if board.mib[x][y] == 0 and board.mab[x] == 0:
            #If any macro is available or the correct macro is selected
            if board.previous_y == -1 or x == board.previous_y:
                #If the micro tile directs to an invalid macro tile
                if board.mab[y] != 0:
                    #Make all macros available
                    board.previous_y = -1
                #Else: direct the next macro to the micro tile's position
                else:
                    board.previous_y = y
                return True
            else:
                print('The move is invalid. Choose a new macro position')
                return False
        else:
            print('The move is invalid. Choose a new position')
            return False
    except:
        print('Position provided is not in domain.')
        return False

#Updates board.mab boards once 3 pieces are connected
def check_micro(x, player):
    micro = board.mib[x]
    #Check if micro is won
    for i in range(0,3):
        #column
        if micro[i] != 0 and micro[i] == micro[i+3] and micro[i] == micro[i+6]:
            board.mab[x] = player
            for tile in range(0,9):
                board.mib[x][tile] = player
            check_macro(x)
            return
        #row
        if micro[(3*i)] != 0 and micro[(3*i)] == micro[(3*i)+1] and micro[(3*i)] == micro[(3*i)+2]:
            board.mab[x] = player
            for tile in range(0,9):
                board.mib[x][tile] = player
            check_macro(x)
            return
        #diagonal
        if micro[0] != 0 and micro[0] == micro[4] and micro[0] == micro[8]:
            board.mab[x] = player
            for tile in range(0,9):
                board.mib[x][tile] = player
            check_macro(x)
            return
        #anti-diagonal
        if micro[2] != 0 and micro[2] == micro[4] and micro[2] == micro[6]:
            board.mab[x] = player
            for tile in range(0,9):
                board.mib[x][tile] = player
            check_macro(x)
            return
        #tie
        if 0 not in micro:
            board.mab[x] = 2
            for tile in range(0,9):
                board.mib[x][tile] = 2
            check_macro(x)
            return

#Check macro
def check_macro(x):
    if x == board.previous_y:
        board.previous_y = -1

    for i in range(0,3):
        #column
        if board.mab[i] != 0 and board.mab[i] != 2 and board.mab[i] == board.mab[i+3] and board.mab[i] == board.mab[i+6]:
            if board.mab[i] == 1:
                print('X has won the game!')
                board.state = 1
            if board.mab[i] == -1:
                print('O has won the game!')
                board.state = -1
            return
        #row
        if board.mab[(3*i)] != 0 and board.mab[(3*i)] != 2 and board.mab[(3*i)] == board.mab[(3*i)+1] and board.mab[(3*i)] == board.mab[(3*i)+2]:
            if board.mab[(3*i)] == 1:
                print('X has won the game!')
                board.state = 1
            if board.mab[(3*i)] == -1:
                print('O has won the game!')
                board.state = -1
            return
        #diagonal
        if board.mab[0] != 0 and board.mab[0] != 2 and board.mab[0] == board.mab[4] and board.mab[0] == board.mab[8]:
            if board.mab[0] == 1:
                print('X has won the game!')
                board.state = 1
            if board.mab[0] == -1:
                print('O has won the game!')
                board.state = -1
            return
        #anti-diagonal
        if board.mab[2] != 0 and board.mab[2] != 2 and board.mab[2] == board.mab[4] and board.mab[2] == board.mab[6]:
            if board.mab[2] == 1:
                print('X has won the game!')
                board.state = 1
            if board.mab[2] == -1:
                print('O has won the game!')
                board.state = -1
            return
        #tie
        if 0 not in board.mab:
            print('It\'s a tie!')
            board.state = 2
            return
