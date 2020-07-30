import numpy as np
import matplotlib.pyplot as pl
from PIL import Image

img = Image.open('perro.jpg')
print(type(img))
print("Size: ",img.size)

array_img = np.asarray(img)

print("Array img: ",array_img)

print(pl.imshow(array_img))
