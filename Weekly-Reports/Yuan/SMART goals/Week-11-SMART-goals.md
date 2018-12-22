## Week 11 SMART Goals

Last week I completed all my goals in that I ran the training scripts and the testing scripts, but I continue to get ‘out of memory’ errors when I  am training. I believe this has to do with the large images in the sample datasets. Running the test scripts are fine and gives me output images, but we can’t input our images into a model that is trained on face or street images.


### SMART Goal 1
##### The first smart goal of the week would be to ask Rex to give me a dataset that has lower resolution like 256x128. So that we can avoid out of memory errors, and train the model on lower resolution images. This can be done within the week, and after receiving the new model, I can just put it on my google drive and copy it over to my google colab environment. 

### SMART Goal 2
##### The second smart goal of the week would be to run the training script on the new lower resolution images, to avoid that out of memory errors. If I continue to run into the error, I will continue to lower the resolution since as long as the image is divisible by 32, the training script should not have any error.

### SMART Goal 3
##### The third smart goal of the week would be to post an issue on github and see if anyone else is able to run vid2vid successfully on one GPU, and on google Colboratory. If someone has tried then I can recieve advice on what to do and what not do, and even if I am able to run it succesfully instead of me trying for weeks on something that ultimatly won't work.

### Stretch goal
##### The stretch goal would be to run vid2vid on our own data, so that we can compare results to pix2pix, and see if it's worth to invest more computing power on vid2vid. This will help our project, because vid2vid has a video discriminator which ensures the optical flow of the output data. This should be done before the end of the semester so we can conclude that vid2vid works with our data and if it's worth an investment. 
 
