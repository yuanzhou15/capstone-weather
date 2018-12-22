# Smart and Stretch Goals

**Name:** Sami
**Date:** Sept 25

## Stretch Goals (1-3)

1. Be able to run pix2pix on the server from start to finish, using many features (from both datasets) as channels  
on multiple GPUS


## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific: 
Modify the pytorch implmentation's stats logger (similar to tensorboard)
  
#### M. Measurable: 
new code will be committed to the repo  

#### A. Achievable:  
Yes, I have a idea on how to proceed.  

#### R. Relevant :
Yes, continuation of previous work.  

#### T. Time-bound: 
1 week  

### S.M.A.R.T. Goal 2.

#### S. Specific: 
Automate running (train/test/organizeresults) pix2pix on combinations of input data.  

#### M. Measurable: 
Code will be added to repo.

#### A. Achievable: 
Yes.  


#### R. Relevant :
Yes, this will make it dead simple to run pix2pix for me and other team members


#### T. Time-bound: 
1 week.   

## S.M.A.R.T. Goals (last week)  


Goal 1. Modify the pytorch implmentation's stats logger (similar to tensorboard):
Done. Visdom can now log any number of input channels. modifications have been made to [this file](https://github.com/yuanzhou15/capstone-weather/blob/master/pytorch-CycleGAN-and-pix2pix/train.py)

Goal 2. Automate running (train/test/organizeresults) pix2pix on combinations of input data:
Done. [massp2p.py](https://github.com/yuanzhou15/capstone-weather/blob/master/sam/run_pix2pix/massp2p.py)
Fully documentated!





