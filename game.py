import rules, board

move_list = []

#Main game loop
def main():
    board.init()
    while rules.game_state() == 0:
        while(not board.set_pos(1, get_move('Player one: '))):
            pass
        board.printb()
        while(not board.set_pos(-1, get_move('Player two: '))):
            pass
        board.printb()

#Handles player input and movement
def get_move(player_name):
    try:
        move = input(player_name).split(' ')
        x = int(move[0])
        y = int(move[1])
        move_list.append((x, y,))
        return (x, y,)
    except:
        print('Invalid input. Retry')
        return (-1, -1,)

if __name__ == '__main__':
    main()
