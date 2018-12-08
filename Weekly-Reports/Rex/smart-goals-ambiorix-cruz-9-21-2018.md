# Smart and Stretch Goals

**Name:** Ambiorix Cruz Angeles
**Date:** 9/21/2018

## Stretch Goals (1-3)

1. Being able to complete one full pipeline from the Feature Team -> Algorithm Team -> Evaluation Team. To be specific, creating a "control" model for comparison between future models. The result of this effort will be shown in the groups documentation file. A table of some sort listing all the future models, including this base model, will be made to keep track of important notes from each model. This is obtainable if everyone in the group puts forth there best effort when it's their teams turn to take over the current model being produced. This is relevant to our project because if we can get into a nice routine, the rest would just be changing the inputs and getting outputs.

## S.M.A.R.T. Goals (next week)

1. Properly Displaying Radar Data
2. Discussing the input sizes and amount of channels with sami's pix2pix and yuans vid2vid
3. Rsyncing and sshing the images onto wproj for the algorithm team to use

Week 4- S.M.A.R.T.- Specific, Measurable, Actionable, Relevant, Timebound

### S.M.A.R.T. Goal 1.

#### S. Specific:
Properly displaying the radar data that professor Brian gave us by re-ranging everything from 0 to np.max() of a given timestamp to 0 with a cap of 30. This will give us  
png images that don't have much of a gradient from black to white. The denser areas of the data will be portrayed as a brightness of 255 which is capped off at 30 mm/hr

#### M. Measurable: 
The result of this effort will be shown by a jupyter notebook titled “rex/radar.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. The idea is to have all of the radar data preserved in some way as png images for the algorithm team to use.

#### A. Achievable:
It is possible for me to achieve this because I've been working with the radar data for a while now and already have some code that was tested before that worked on singular instances. My computer at home is more than capable of doing this task in a jupyter notebook environment through anaconda navigator.

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. The radar images are the bread and butter of this whole operation. If these images can be processed now, then we are 1 step closer to completing the stretch goal.

#### T. Time-bound:
This task should be done by next Sunday. 9/30/2018

### S.M.A.R.T. Goal 2.

#### S. Specific:
Discussing the exact pixel width and height of the images that sami's pix2pix algorithm will use and yuan's vid2vid algorithm will use.

#### M. Measurable:
The result of this effort will be shown by a jupyter notebook titled “rex/png-resize.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. Any interesting finds will be documented on the notebook itself as well as on the wiki page.

#### A. Achievable:
It is possible for me to achieve this because all of the data is stored onto my 2 TB HDD that I got for this class. My computer at home is more than capable of doing this task in a jupyter notebook environment through anaconda navigator. If need be, a linux virtual environment will be used inside my home computer. In addition, a python library by the name of pillow is used as the standard image processing library for python.

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. These several models will then be examined and evaluated based on how accurately they reproduce the available radar image. The model's being trained by sami and yuan require very specific png image dimensions to work. For example, the png images for pix2pix have to be square and divisible by 32.

#### T. Time-bound:
This task should be done by next Sunday. 9/30/2018

### S.M.A.R.T. Goal 3.

#### S. Specific:
Rsync the generated png images onto a computer in the linux lab from home. Then, ssh into that computer and rsync the files again to wproj.

#### M. Measurable:
The result of this effort will be shown by a folder in the scratch folder in wproj titled "images".

#### A. Achievable:
All of the images have been created and it's just a matter of properly rsyncing and sshing without any errors.

#### R. Relevant:
Since the data will be on the wproj node, sami and yuan may begin their work.

#### T. Time-bound:
This task should be done by next Sunday. 9/30/2018 

## S.M.A.R.T. Goals (last week)

Smart Goal #1- "Extracting the model data" notebook: https://github.com/rhaxx/capstone-weather/rex/radnote.ipynb

Smart Goal #2- "Learning to use rsync to push data to wproj"

Smart Goal #3- "Using Basemap to crop and plot model data" https://github.com/yuanzhou15/capstone-weather/wiki/Feature-Team
