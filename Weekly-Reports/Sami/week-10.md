# Smart and Stretch Goals

**Name:** Sami
**Date** In no order

## Stretch Goals

1. Use what we have to get best possible results

## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific:   
train new models using new data (model data, 5 bands satellite). prepare for meeting with prof. brian.   

#### M. Measurable: 
Yes

#### A. Achievable:  
Yes.

#### R. Relevant :
Yes.

#### T. Time-bound: 
1 week  


## S.M.A.R.T. Goals (last 2 week)  

Goal 1. vid2vid debugging
Investigated the code on the server. Got same conclusion as yuan, that the K80 GPU architecture is not correctly supported in vid2vid.  
So, I went ahead and installed Ubuntu on a dedicated hard drive on my machine, which has a more modern GPU architecture, yet a weaker gpu, to get to the bottom of the problem.  
I setup docker and other required software, and managed to get everything ready. When i ran finally ran vid2vid I ran out of memory, apparently no less than 8GB of gpu memory is required.
My Nvidia 1060 gpu only has 6GB.  
Then I also tried it on google collab, but before finishing, yuan was successful in running it on google cloud. 
The only material to support my claims, is the dedicated hard drive with ubuntu and the software on it.
