## Week 12 SMART Goals

Last week I was able to run vid2vid on the lower resolution images that Rex gave me, and I no longer ran into out of memory errors, but I’m still hitting “No Cuda image found on machine”. My goals this week address this problem

### SMART Goal 1
##### The first goal of this week is to go back on the issues page, and become more active. Another user stated that Flownet does not support the Tesla V80 GPU architectures, and both the machines given to us and google colab are V80 GPUs, so in this case, I would need to ask around and see how people overcome this obstacle. I would need to do more research and look through Flownet’s setup code and find where it is that proves that V80 architecture is not supported

### SMART Goal 2
##### The second goal of this week would be to work together with Sami, since Sami has a personal GPU that’s not V80 and so we can try training on his GPU and see if we can get results that way. I would have to walk Sami through all the setup so that he doesn’t have to research on how to set up vid2vid and we can get to training right away.


### SMART Goal 3
##### The third goal would be to look into AWS and GCP and see if I can get a single GPU instance that I can begin to work on. I know that both AWS and GCP offers gpus and charge on a hourly basis, and AWS has a instance limit, so I will have to apply to GPU on both platforms and see which one gives me a GPU without a problem so I can start running vid2vid on another gpu architecture. 

### Stretch goal
##### The stretch goal would be to run vid2vid on our own data, so that we can compare results to pix2pix, and see if it's worth to invest more computing power on vid2vid. This will help our project, because vid2vid has a video discriminator which ensures the optical flow of the output data. This should be done before the end of the semester so we can conclude that vid2vid works with our data and if it's worth an investment. 
 