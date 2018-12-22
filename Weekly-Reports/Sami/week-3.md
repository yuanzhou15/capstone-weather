# Smart and Stretch Goals

**Name:** Sami
**Date:** Sept 18

## Stretch Goals (1-3)

1. Be able to run pix2pix on the server from start to finish, using many features (from both datasets) as channels  
on multiple GPUS


## S.M.A.R.T. Goals (next week)

### S.M.A.R.T. Goal 1.

#### S. Specific: 
Write a custom data loader for the new PyTorch pix2pix implementation  
  
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
Test the new PyTorch implementation on multichannel satellite input    

#### M. Measurable: 
code/scripts for preprocessing the data will be added to the repo, 
as well as train/test output folders on the server  

#### A. Achievable: 
Yes.  


#### R. Relevant :
Yes, this is why're using a new pix2pix implementation in the first place  


#### T. Time-bound: 
1 week.   
  

### S.M.A.R.T. Goal 3.  
  
#### S. Specific:  
If above goals are successful, start working with feature team on incorporating Model data into pix2pix input  


#### M. Measurable: 
scripts/code will be added  
as well as train/test output folders on the server  


#### A. Achievable: 
Yes, if the above 2 goals went as expected.  

  
#### R. Relevant:  
Very. adding model data as input should improve gemerated images   


#### T. Time-bound: 
Depends on the 2 goals above, and on how easily I can mae use of feature team's work.   


## S.M.A.R.T. Goals (last week)  


Goal 1. Multi-channel pix2pix input:  
Ended-up using a new implementation in PyTorch.   
After investigation and reading the code, it turns out I need to write a custom data loader.  
So, not fully finished yet, but a huge step forward.  
[the new implementation](https://github.com/yuanzhou15/capstone-weather/tree/master/pytorch-CycleGAN-and-pix2pix)
PyTorch and the implementation have been installed and tested on the server.  
[New scripts](https://github.com/yuanzhou15/capstone-weather/tree/master/sam/run_pix2pix) for using it have been added

Goal 2. Make use of 2nd GPU for GAN training:  
The new implementation can use multiple GPU's depending on the "batch size" and the specified GPU id's.  
So [A new script](https://github.com/yuanzhou15/capstone-weather/blob/master/sam/run_pix2pix/pytorch_train.sh) for training has been added.  
nvidia-smi now shows 2 GPUs are being used during training.  
   
Goal 3. Re-run using modified radar images:  
The new radar images seems to have more details now, which is good. but not a huge improvement.  
Which means features team need to consult with brian to sort this out for good.  
[New radar preprocessing](https://github.com/yuanzhou15/capstone-weather/blob/master/src/wdata.py#L17)   
and [visualization/debugging notebook](https://github.com/yuanzhou15/capstone-weather/blob/master/sam/investigate_radar.ipynb)  
input/output images, train/test/model output folders on the server (folder "run2") 





