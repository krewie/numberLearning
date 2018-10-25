import numpy as np

def normalizeInput(twoDArray):
    twoDArray[twoDArray == 0] = 1
    twoDArray[twoDArray == 255] = 0
    return twoDArray

def normalizeInput_training(twoDArray):
    twoDArray[twoDArray == 0] = 1
    twoDArray[twoDArray > 1] = 0
    return twoDArray
