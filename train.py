from mnist import MNIST
import random
import numpy as np
import normalizer

mndata = MNIST('../../training_data/MNISTData')

images, labels = mndata.load_testing()

index = random.randrange(0, 50)

print(mndata.display(images[45]))

print(images[45])

## Turn flat list into 2D array

arr = np.array(images[45]).reshape(-1, 28)

normalized_input = normalizer.normalizeInput_training(arr)

print(arr)