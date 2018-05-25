import board, rules, ai

#
class Node():

    def __init__(self, parent=None, state=None):
        #The state is an array of data containing 9 arrays for
        #each micro board, an array of all macro tiles, an array
        #of all valid/invalid moves, which player has filled each
        #macro, tile which turn it is, and the active sector[s]
        #         0  1  2  3  4  5  6  7  8    9     10   11   12    13
        #state = [b0,b1,b2,b3,b4,b5,b6,b7,b8,macro,valid,fill,turn,sectors]
        self.state = state
        self.parent = parent
        self.child = None
        self.value = 0 #N
        self.visits = 0 #W
        self.probability = 0.0 #P

    #Expand the node for all possible moves and evaluate the best child
    def expand():
        move_list = []
        for ma, active_sector in enumerate(self.state[13]):
            for mi, tile in enumerate(active_sector):
                if tile == 0:
                    move_list.append((ma, mi))
        for move in move_list:
            state_copy = self.state
            state_copy[move[0]][move[1]] = self.state[12]
            state_copy = rules.check_mcts(state_copy)
            self.probability = eval.evaluate(state_copy)

    #Plays a piece to simulate the rules of the game

    #Selects the
    def select():

    #Moves the value and visit scores up the parent tree
    def backpup():
