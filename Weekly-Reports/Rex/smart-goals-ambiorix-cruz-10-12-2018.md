# Smart and Stretch Goals

**Name:** Ambiorix Cruz Angeles
**Date:** 10/12/2018

## Stretch Goals (1-3)

1. Being able to complete one full pipeline from the Feature Team -> Algorithm Team -> Evaluation Team. To be specific, creating a "control" model for comparison between future models. The result of this effort will be shown in the groups documentation file. A table of some sort listing all the future models, including this base model, will be made to keep track of important notes from each model. This is obtainable if everyone in the group puts forth there best effort when it's their teams turn to take over the current model being produced. This is relevant to our project because if we can get into a nice routine, the rest would just be changing the inputs and getting outputs.

## S.M.A.R.T. Goals (next week)

1. Talk with sami about sampling non sparse radar images
2. Talk with yuan to get her vid2vid working on band 2 with radar alone
3. Updating the wiki page!

Week 7- S.M.A.R.T.- Specific, Measurable, Actionable, Relevant, Timebound

### S.M.A.R.T. Goal 1.

#### S. Specific:
Converse with sami about way sampling out the sparse radar images.

#### M. Measurable: 
The result of this effort will be shown by a jupyter notebook titled “rex/radar.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. The idea is to sample out any really good radar images.

#### A. Achievable:
This is achievable using pythons matplotlib, pillow, and numpy library. 

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. Removing the really sparse radar images could help the models become better at predicting the radar image values if we know their is precipitation happening at that specific time.

#### T. Time-bound:
This task should be done by next Sunday. 10/21/2018

### S.M.A.R.T. Goal 2.

#### S. Specific:
Conversing with yuan about how to shape the images to better fit vid2vid. Possibly only using band 2 and radar to start.

#### M. Measurable:
The result of this effort will be shown by a jupyter notebook titled "rad_sat_mod.ipynb" in the rex folder of the master repo.

#### A. Achievable:
It is possible for me to achieve this because all I have to do is use pythons pillow library to resize the images and the os library to move or rename the files.

#### R. Relevant:
Vid2vid takes into account previous timesteps as will as future timesteps when training the model. Something pix2pix does not do.

#### T. Time-bound:
This task should be done by next Sunday. 10/21/2018

### S.M.A.R.T. Goal 3.

#### S. Specific:
Update the wiki page!

#### M. Measurable:
The result of this effort will be shown by a wiki page on the master repo titled feature team.

#### A. Achievable:
The wiki page was already created and updating it isn't that hard.

#### R. Relevant:
Incase someone would like to dive deep into what we achieved or if I ever need to go back to review some aspects of the project.

#### T. Time-bound:
This task should be done by next Sunday. 10/21/2018 

## S.M.A.R.T. Goals (last week)

Smart Goal #1- "Generating the rest of the 20 hours from each dataset for sami's pix2pix" notebook: https://github.com/yuanzhou15/capstone-weather/rex/satellite.ipynb  
https://github.com/yuanzhou15/capstone-weather/rex/model.ipynb  
https://github.com/yuanzhou15/capstone-weather/rex/radar.ipynb

Smart Goal #2- "Adding on more information to the feature teams wiki page" https://github.com/yuanzhou15/capstone-weather/wiki/Feature-Team

Smart Goal #3- "Renaming the model data png images to match that of the new satellite and radar images for sami"