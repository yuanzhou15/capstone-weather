## Week 13 SMART Goals

Last week I was able to look into GCP and AWS to get a single GPU to train vid2vid, and I was able to get a single GPU on GCP while AWS asked me to put in an issue to use a GPU since I have to increase my instance limit. The goals this week are the next steps to train on out data.

### SMART Goal 1
##### The first goal of this week, would be to work with Sami’s GPU since he continues to get “out of memory errors” in his GPU. We can continue to decrease the image size so that we can avoid this issue. If we can get past this and successfully run vid2vid then I won’t have to buy a GPU from GCP. 

### SMART Goal 2
##### The second goal would be to set up the GCP instance with all the dependencies that vid2vid requries, like CUDA 9.2, CuDNN, and all the pip libraries. This is important since the gpu on GCP is a Tesla V100, so if all the setup goes well, then we should be able to run vid2vid training on our data. 

### SMART Goal 3
##### The third goal would be to figure out how I can get data onto my GPU instance. This is  the first time I’ve worked with a gpu on Google Cloud Computing, and the gpu instance is something I SSH into, so I would need to figure out how to get data on there so that I can train on our weather data instead of the sample data that vid2vid provides for me through their script. 

### Stretch goal
##### The stretch goal would be to run vid2vid on our own data, so that we can compare results to pix2pix, and see if it's worth to invest more computing power on vid2vid. This will help our project, because vid2vid has a video discriminator which ensures the optical flow of the output data. This should be done before the end of the semester so we can conclude that vid2vid works with our data and if it's worth an investment. 