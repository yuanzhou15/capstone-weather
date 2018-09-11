import numpy as np

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray;

def rgb2red(rgb):
    return rgb[:,:,0]

def rgb2green(rgb):
    return rgb[:,:,1]

def rgb2blue(rgb):
    return rgb[:,:,2]
    

