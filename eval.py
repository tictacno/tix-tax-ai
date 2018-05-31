import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

#Unpacks game state into list of data
def linearize(state):
    data = []
    for item in state:
        for piece in item:
            data.append(piece)
    return data

def evaluate(state, move_number):
    data = linearize(state)

    return 0.0
