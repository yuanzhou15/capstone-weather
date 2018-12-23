## Week 7 SMART Goals

From last week even after several fresh installs, I am still encountering the same errors of no CUDA image found on device. The goals this week addresses what I plan to do this week to address those errors. 

### SMART Goal 1
##### The first goal of this week would be to ask Paul if it was possible to update gcc, since that was a warning I encountered during the set up of Flownet that I can not take of with out root access. If this warning is taken care of then I can run vid2vid again and see if after taking care of all the warning, I am able to trian vid2vid without any errors. This goal can be measured by having gcc updated on the node

### SMART Goal 2
##### The second goal of the week would be to follow up with the issue I posted on github. Another user is also getting the same error and implies that it could be an issue while setting up FlowNet. So this week I will be posting on FlowNet's issue page and see if anyone is having the same issue that I am. This goal can be measured by issue postings I posted on both vid2vid and FlowNet's github page

### SMART Goal 3
##### The third goal of the week would to re run vid2vid after gcc is updated if Paul responds. gcc is the only warning that I can't take care of without root access, so this run of vid2vid will let me know if all the warnings are the cause of the errors or not.

### Stretch goal
##### The stretch goal would be to run vid2vid on our own data, so that we can compare results to pix2pix, and see if it's worth to invest more computing power on vid2vid. This will help our project, because vid2vid has a video discriminator which ensures the optical flow of the output data. This should be done before the end of the semester so we can conclude that vid2vid works with our data and if it's worth an investment. 