# Smart and Stretch Goals

**Name:** Ambiorix Cruz Angeles
**Date:** 11/9/2018

## Stretch Goals (1-3)

1. Being able to complete one full pipeline from the Feature Team -> Algorithm Team -> Evaluation Team. To be specific, creating a "control" model for comparison between future models. The result of this effort will be shown in the groups documentation file. A table of some sort listing all the future models, including this base model, will be made to keep track of important notes from each model. This is obtainable if everyone in the group puts forth there best effort when it's their teams turn to take over the current model being produced. This is relevant to our project because if we can get into a nice routine, the rest would just be changing the inputs and getting outputs.
Update: We have completed our stretch goal. Now all we have to do is compare and contrast different trained models.


## S.M.A.R.T. Goals (next week)

1. Mimicing the cityscape dataset for Yuan's vid2vid.

2. Rotating Sami's dataset to quadrouple it.

3. Giving Satyam the numpy versions of the png images.

Week 11- S.M.A.R.T.- Specific, Measurable, Actionable, Relevant, Timebound

### S.M.A.R.T. Goal 1.

#### S. Specific:
Yuan requested to create a train_A, train_B, test_A, and test_B folders. Each folder should contain subfolders in sequential order: 000, 001, 002, etc. Each sequential folder should contain a series of images of length 30 or more that have no gaps. If an hour is missing, the series is broken. For simplicity, I will only be giving her satellite band 2 images and radar images.

#### M. Measurable: 
The efforts of this adventure can be measured by the amount of code written in a jupyter notebook titled "reorganized" in the rex subfolder of the master repository.

#### A. Achievable:
All of the data is available to me and is ready for manipulation. Using the pillow library to read in the images, rotate them, and save them.

#### R. Relevant:
rotated data can help sami's model become more generalized to all forms of

#### T. Time-bound:
This task should be done by next Sunday. 11/18/2018

### S.M.A.R.T. Goal 2.

#### S. Specific:
Since sami's dataset is rather small, rotating the images by 90 degrees counterclockwise and saving it as an entirely new image (x3) should give us more "images" even though we don't have any more actual hours.

#### M. Measurable:
Most of this effort will be shown by the "rotated" jupyter notebook in the rex subfolder for the master repository.

#### A. Achievable:
All of the data is available to me and is ready for manipulation. Using the pillow library to read in the images, rotate them, and save them.

#### R. Relevant:
rotated data can help sami's model become more generalized to all forms of inputs.

#### T. Time-bound:
This task should be done by next Sunday. 11/18/2018

### S.M.A.R.T. Goal 3.

#### S. Specific:
Satyam doesn't need to work with png images. So, it was decided that I give him the numpy versions of the data so he can work closer to the real numbers.

#### M. Measurable:
The result of this effort will be shown by two jupyter notebooks titled "satyam_rad_sat" and "satyam_rad_sat_mod."

#### A. Achievable:
I have already made jupyter notebook to generate the png image version of all the data.

#### R. Relevant:
He can run a feature importance and multi linear regression on the raw data to help us choose better inputs for pix2pix

#### T. Time-bound:
This task should be done by next Sunday. 11/18/2018 

## S.M.A.R.T. Goals (last week)

Smart Goal #1- "Experimenting with sci-kit images canny edge detection" notebook:
https://github.com/yuanzhou15/capstone-weather/blob/master/rex/edge-detection.ipynb

Smart Goal #2- "Managing all of the datasets from sami, yuan, and satyam" notebook: https://github.com/yuanzhou15/capstone-weather/tree/master/rex

Smart Goal #3- "Updating the Feature Team Wiki Page!"
https://github.com/yuanzhou15/capstone-weather/wiki/Feature-Team