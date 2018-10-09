import normalizer
import numpy as np
import PIL
from ui import init
from neuralnetwork import NeuralNetwork

init()

img = PIL.Image.open("image.png").convert("L")
imgarr = np.array(img)

print("imagearray created")

np.set_printoptions(threshold=np.nan)
normalized_input = normalizer.normalizeInput(imgarr)

nn = NeuralNetwork(normalized_input, np.ndarray(shape=(10)))

nn.feedforward()

print(nn.result())