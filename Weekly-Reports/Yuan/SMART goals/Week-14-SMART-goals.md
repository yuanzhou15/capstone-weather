## Week 14 SMART Goals

Last week I was able to successfully run the training script of vid2vid on our data set. This week’s goals are my steps to take after training.

### SMART Goal 1
##### The first goal would be to change video lengths to a larger number like 30, because when I trained on a smaller sequence length, I got completely dark images as outputs. So I need to increase the sequence length. This will cut down significantly how much data we can use to train the model, but hopefully will give us some results so that we can see if  vid2vid is a valid model that can help solve our problem.

### SMART Goal 2
##### The second goal would be to organize all the corresponding satellite and radar images together so that I can give the results to the evaluating team to evaluate the results that vid2vid gave. The results probably won’t be good, since length 30 video sequences are quite long, and it will cut down the total training images to 180, which is nowhere near enough to train a deep learning model.

### SMART Goal 3
##### The third goal of the week would be to put the outputted images into a video so that we can see if the optical flow is smooth. The whole point of vid2vid is that we hope it will output smooth images so we won’t have random clouds appear out of nowhere. When I put the outputted images into a video, I can then present the optical flow of the predicted images.

### Stretch goal
##### The stretch goal would be to run vid2vid on our own data, so that we can compare results to pix2pix, and see if it's worth to invest more computing power on vid2vid. This will help our project, because vid2vid has a video discriminator which ensures the optical flow of the output data. This should be done before the end of the semester so we can conclude that vid2vid works with our data and if it's worth an investment. 
