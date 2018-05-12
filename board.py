import numpy as np, math
import rules, game

mab = [] #MAcro Board
mib = [] #MIcro Board

# Board layout:
# [0][1][2]
# [3][4][5]
# [6][7][8]

#Gets the player at a given location
def get_pos(pos):
    return mib[pos[0]][pos[1]]

#Checks if position is open then sets position to player's id
def set_pos(player, pos):
    x = pos[0]
    y = pos[1]
    if (x + y) > 0 and x < 9 and y < 9:
        if rules.valid_move(x, y):
            mib[x][y] = player
            rules.update_board(x, player)
            return True
        else:
            return False
    else:
        print('Position provided is not in domain.')
        return False

#Prints the board's current state
def printb():
    lines = []
    for i in range(0, 9):
        lines.append('')
    for mi, micro in enumerate(mib):
        for ti, tile in enumerate(micro):
            if ti < 3:
                lines[(3*math.floor(mi/3))] = str(tile)
            elif ti < 6:
                lines[(3*math.floor(mi/3))+1] = str(tile)
            else:
                lines[(3*math.floor(mi/3))+2] = str(tile)
    for line in lines:
        print(line)

#Initializes board positions
def init():
    for i in range(0, 9):
        mab.append(0)
        mib.append([0,0,0, 0,0,0, 0,0,0])
