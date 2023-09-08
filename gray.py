import cv2
import numpy as np

im = cv2.imread("C:\Users\hoshi\OneDrive\デスクトップ\Geeksalon\Product\salad_chicken.jpg")
print(im.shape)
# (225, 400, 3)

print(im.dtype)
# uint8