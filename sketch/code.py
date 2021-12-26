import numpy as np
import imageio
import cv2
import scipy.ndimage
from sys import argv

img = argv[1]
file = img.split('.')

def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.2989,0.5870,0.1140])

def dodge(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')

S = imageio.imread(img)
g = grayscale(S)
i = 255 - g

b = scipy.ndimage.filters.gaussian_filter(i, sigma = 10)
r = dodge(b, g)
# Write's to file and saves it has filename_final.extension
cv2.imwrite(f"{file[0]}_final.{file[1]}", r)
