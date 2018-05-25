import numpy as np, math
import rules, game, ai

mab = [] #MAcro Board
mib = [] #MIcro Board

# Board layout:
# [0][1][2]
# [3][4][5]
# [6][7][8]

#Previous micro position (current macro)
previous_y = -1 # -1 means any macro

#0 (running), 1 (player 1 win), -1 (player 2 win), or 2 (draw)
state = 0

#Gets the player at a given location
def get_pos(pos):
    return mib[pos[0]][pos[1]]

#Checks if position is open then sets position to player's id
def set_pos(player, pos):
    x = pos[0]
    y = pos[1]
    if  x > -1 and y > -1 and x < 9 and y < 9:
        if rules.valid_move(x, y):
            mib[x][y] = player
            rules.check_micro(x, player)
            return True
        else:
            return False
    else:
        print('Position provided is not in domain.')
        return False

#Prints the board's current state
#Needs fixing
def printb():
    lines = []
    for i in range(0, 9):
        lines.append('')
    for mi, micro in enumerate(mib):
        for ti, tile in enumerate(micro):
            if ti < 3:
                lines[(3*math.floor(mi/3))] += str(tile) + ' '
            elif ti < 6:
                lines[(3*math.floor(mi/3))+1] += str(tile) + ' '
            else:
                lines[(3*math.floor(mi/3))+2] += str(tile) + ' '
    for line in translate(lines):
        print(line)

#Translates board to readable list
def translate(lines):
    res = []
    for l, line in enumerate(lines):
        line_parts = line.split(' ')
        new_line = ''
        if (l % 3) == 0 and l != 0:
            res.append(new_line)
        for i, s in enumerate(line_parts):
            if s == '0':
                new_line += '_'
            if s == '1':
                new_line += 'X'
            if s == '-1':
                new_line += 'O'
            if s == '2':
                new_line += 'T'
            if (i % 3) == 2:
                new_line += '  '
        res.append(new_line)
    res.append('')
    return res

#Initializes board positions
def init():
    for i in range(0, 9):
        mab.append(0)
        mib.append([0,0,0, 0,0,0, 0,0,0])
