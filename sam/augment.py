import Augmentor
import numpy as np
from PIL import Image
import glob
import os
import random

def rot(path,savedir):
    p = Augmentor.Pipeline(path, save_format='png', output_directory=savedir)
    p.rotate90(1)
    p.process()

def flip(path,savedir):
    p = Augmentor.Pipeline(path, save_format='png', output_directory=savedir)
    p.flip_left_right(1)
    p.process()

paths = [
    "/home/wproj/scratch/augmented/train/A1",
    "/home/wproj/scratch/augmented/train/A2",
    "/home/wproj/scratch/augmented/train/A3",
    "/home/wproj/scratch/augmented/train/A4",
    "/home/wproj/scratch/augmented/train/A5",
    "/home/wproj/scratch/augmented/train/B"
]

for pa in paths:
    flip(pa, pa.replace('train', 'flip_l_r'))

for pa in paths:
    rot(pa, pa.replace('train', 'rot90'))

print("Done.")
