import numpy
import PIL
from ui import init

init()

img = PIL.Image.open("image.png").convert("L")
imgarr = numpy.array(img)

print("imagearray created")

numpy.set_printoptions(threshold=numpy.nan)
print(imgarr)