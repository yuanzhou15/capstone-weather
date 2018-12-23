## Week 8 SMART Goals

since last week, Paul responded to my emails saying that he is not able to updated the gcc version since I am sharing the machine with others. My goals this week address what I will do next to get vid2vid to train on our data. 

### SMART Goal 1
##### Since Paul won't be updating the gcc version, I won't be able to get rid of all the warning I get when I set up vid2vid. I will re install vid2vid regardless and see if vid2vid will still train with out the latest version of  gcc. If it will train then I won't have to worry about getting the latest version of gcc. 

### SMART Goal 2
##### Another goal this week would be to look into google colaboratory since I get a free GPU with it. I should set up an google colaboratory doc, so that I can start setting up the environment for vid2vid. This will be convenient for the project since I will be working on a seperate machine than pix2pix, and I won’t have to worry about updating anything without interfering with other people’s work. Working on colab will give me the freedom to install / update whatever software I see fit. 

### SMART Goal 3
##### The GPU on google colaboratory is the same GPU as the machines given to us, Tesla V80. However CUDA is not installed, so another goal this week is to set up a NVIDIA account and obtain a run file of CUDA 9.2 that upload that to my google drive, so that my colaboratory jupyter notebook can use that file to install CUDA 9.2. Having CUDA on colab is important because I need it to run vid2vid. 

### Stretch goal
##### The stretch goal would be to run vid2vid on our own data, so that we can compare results to pix2pix, and see if it's worth to invest more computing power on vid2vid. This will help our project, because vid2vid has a video discriminator which ensures the optical flow of the output data. This should be done before the end of the semester so we can conclude that vid2vid works with our data and if it's worth an investment. 