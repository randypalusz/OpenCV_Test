import numpy as np
import cv2
import Util
from matplotlib import pyplot as plt

im = cv2.imread('images/castle.png')
im2 = cv2.imread('images/baboon.png')
cv2.imshow('test', im)

# visualize bgr in respective channels
# Util.showbgr(im)

# split image into b, g, r channels, costly
# b, g, r = cv2.split(im)
# using numpy
# b, g, r = Util.split(im)

# Border Demonstration
# Util.showallborders(im, bw=40)

# Blending Example
Util.showblend(im, im2)

# following two lines are to wait until key is pressed to terminate all shown windows
cv2.waitKey(0)
cv2.destroyAllWindows()
