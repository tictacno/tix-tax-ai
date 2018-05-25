import rules, board, ai

move_list = []

#Main game loop
def main():
    print('\nAlephT Ultimate Tic Tac Toe Engine by Geo')
    print('For information about the game type \'info\'')
    board.init()
    board.printb()
    while board.state == 0:
        while(not board.set_pos(1, get_move('X: '))):
            pass
        board.printb()
        if board.state != 0:
            return
        while(not board.set_pos(-1, get_move('O: '))):
            pass
        board.printb()
        if board.state != 0:
            return

#Handles player input and movement
def get_move(player_name):
    try:
        move = input(player_name).split(' ')
        if move[0] == 'info':
            info()
            return (-1, -1,)
        x = int(move[0])
        y = int(move[1])
        move_list.append((x, y,))
        return (x, y,)
    except:
        print('Invalid input. Retry')
        return (-1, -1,)

#Prints info about the game
def info():
    print('AlephT v0.1 by Geo\n')

if __name__ == '__main__':
    main()
