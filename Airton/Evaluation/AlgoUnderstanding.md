# Pix2Pix

## This document is to write down the understanding of the algorithm I will be evaluation through its outputs <br/>

## Basic Understanding <br/>

### First 
The pix2pix takes in input A and will be placed it in folder A. <br/>

### Second
The target images will be B and will be placed in folder B.<br/>

### Third
Then A and B are taken and combined into a single image that is placed in a folder combined.<br/>

### Fourth
Pix2pix now takes the combined and splits it into two sets, train and validation.<br/> 

### Fifth
It trains on the GAN model only with the train set and produces it first output on a folder called train_out. 
The train_out folder contains the tensorboard graph, which has the info and visualization that are useful and we can alter and the predicted images that are created from the training images (the predicted images are predicted from the validation set, which GAN wasn’t trained on). 




