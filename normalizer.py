import numpy as np

def normalizeInput(twoDArray):
    twoDArray[twoDArray == 0] = 1
    twoDArray[twoDArray == 255] = 0
    return twoDArray
