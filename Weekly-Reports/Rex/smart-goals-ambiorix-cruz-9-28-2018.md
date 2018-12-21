# Smart and Stretch Goals

**Name:** Ambiorix Cruz Angeles
**Date:** 9/28/2018

## Stretch Goals (1-3)

1. Being able to complete one full pipeline from the Feature Team -> Algorithm Team -> Evaluation Team. To be specific, creating a "control" model for comparison between future models. The result of this effort will be shown in the groups documentation file. A table of some sort listing all the future models, including this base model, will be made to keep track of important notes from each model. This is obtainable if everyone in the group puts forth there best effort when it's their teams turn to take over the current model being produced. This is relevant to our project because if we can get into a nice routine, the rest would just be changing the inputs and getting outputs.

## S.M.A.R.T. Goals (next week)

1. Extracting satellite band 3, 4, and 6 for sami
2. Creating and documenting the findings down on the feature team wiki page
3. Renaming the model data png images to match that of the new satellite and radar images for sami

Week 5- S.M.A.R.T.- Specific, Measurable, Actionable, Relevant, Timebound

### S.M.A.R.T. Goal 1.

#### S. Specific:
Extracting images from satellite band 3,4, and 6 for sami with the new folder and filename construction.

#### M. Measurable: 
The result of this effort will be shown by a jupyter notebook titled “rex/satellite.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. The idea is to properly label the input images and the "supervised" input images so that the pix2pix algorithm can properly match them up.

#### A. Achievable:
This is achieavle using pythons os library for file renaming and copying. folder A must contain inputs and folder B will contain the relevant correlating radar input.

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. Properly naming all the files will allow the algorithm team to progress further so we can reach our stretch goal faster.

#### T. Time-bound:
This task should be done by next Sunday. 10/7/2018

### S.M.A.R.T. Goal 2.

#### S. Specific:
Creating a wiki page specifically for what i'm doing in the feature team. It will mostly retain information about how the data is stored on the hdd.

#### M. Measurable:
The result of this effort will be shown by a wiki page titled "feature team" in the master repo. 

#### A. Achievable:
It is possible for me to achieve this because all I have to do is create the wiki page and structure it to mimic what I've been doing as well as what is on the hdd itself.

#### R. Relevant:
Documentation is key incase something goes wrong or the future me would like to go back and look over old code or certain aspects of this project. The more organized we are now, the easier of a time the future me will have.

#### T. Time-bound:
This task should be done by next Sunday. 10/7/2018

### S.M.A.R.T. Goal 3.

#### S. Specific:
Rename the model data png images to match that of the satellite and radar, with the exception of the new A# that will correlate to being model data.

#### M. Measurable:
The result of this effort will be shown by a jupyter notebook in the "rex/model.ipynb" on the master repo.

#### A. Achievable:
All of the images have to created and it's just a matter of properly renaming them with the new format.

#### R. Relevant:
Furthers sami's pix2pix model progression

#### T. Time-bound:
This task should be done by next Sunday. 10/7/2018 

## S.M.A.R.T. Goals (last week)

Smart Goal #1- "Properly displaying radar images" notebook: https://github.com/yuanzhou15/capstone-weather/rex/radar.ipynb

Smart Goal #2- "Discussing the input sizes and amount of channels with sami's pix2pix and yuans vid2vid"

Smart Goal #3- "Rsyncing and sshing the images onto wproj for the algorithm team to use"
