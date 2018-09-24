# Smart and Stretch Goals

**Name:** Ambiorix Cruz Angeles
**Date:** 9/17/2018

## Stretch Goals (1-3)

1. Being able to complete one full pipeline from the Feature Team -> Algorithm Team -> Evaluation Team. To be specific, creating a "control" model for comparison between future models. The result of this effort will be shown in the groups documentation file. A table of some sort listing all the future models, including this base model, will be made to keep track of important notes from each model. This is obtainable if everyone in the group puts forth there best effort when it's their teams turn to take over the current model being produced. This is relevant to our project because if we can get into a nice routine, the rest would just be changing the inputs and getting outputs.

## S.M.A.R.T. Goals (next week)

1. Learn how to use xarray to make correlating/working with the data easier.
2. Perform a sanity-check with the data so that it is over our domain. From all three sources.
3. Work with sami to construct a function that will allow us to input an image using all three channels of pix2pix.

Week 2- S.M.A.R.T.- Specific, Measurable, Actionable, Relevant, Timebound

### S.M.A.R.T. Goal 1.

#### S. Specific:
Now that the model data has been updated and almost quadroupled in size, it's time to run the feature-extract notebook on it. The goal is to update the previously extracted features so that now will be on par with satellite and radar data's frequency (every hour or so).

#### M. Measurable: 
The result of this effort will be shown by a jupyter notebook titled “rex/feature-extract.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. If i can find a way to optomize the function, perhaps extraction 2-3 features as i pass once through all the data, then i will do that.

#### A. Achievable:
It is possible for me to achieve this because I've been working with the model data for a while now and already have some code that was tested before that worked on the previous much smaller model data set. My computer at home is more than capable of doing this task in a jupyter notebook environment through anaconda navigator.

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. These several models will then be examined and evaluated based on accurately they reproduce the available radar image. This task will help us get more correlating data for model training.

#### T. Time-bound:
This task should be done by next Sunday. 9/23/2018

### S.M.A.R.T. Goal 2.

#### S. Specific:
Re-running the correlation.ipynb so that it'll now also go through the new model data (.npy) files and find out which ones correlate with the radar and sat data.

#### M. Measurable:
The result of this effort will be shown by a jupyter notebook titled “rex/correlate.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. Any interesting finds will be documented on the notebook itself as well as on the wiki page.

#### A. Achievable:
It is possible for me to achieve this because all the raw data is stored onto my 2 TB HDD that I got for this class. My computer at home is more than capable of doing this task in a jupyter notebook environment through anaconda navigator. If need be, a linux virtual environment will be used inside my home computer.

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. These several models will then be examined and evaluated based on how accurately they reproduce the available radar image. More data that correlates means more data to train on for a model.

#### T. Time-bound:
This task should be done by next Sunday. 9/23/2018

### S.M.A.R.T. Goal 3.

#### S. Specific:
I will try to create and optomize a model using keras that will be trained on one model data and used to generate/predict another model data feature.

#### M. Measurable:
The result of this effort will be shown by a jupyter notebook titled “rex/keras.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. 

#### A. Achievable:
All of the model data is already available for me to use and keras is very well documented. There are plenty of tutorials online as well to help create some simple models.

#### R. Relevant:
At the end of the semester, everyone should have there own subproject that they have can say they did as well as the bigger group project.

#### T. Time-bound:
This task should be done by next Sunday. 9/23/2018 

## S.M.A.R.T. Goals (last week)

Smart Goal #1- "Re-exploring radar data" notebook: https://github.com/rhaxx/capstone-weather/rex/radnote.ipynb

Smart Goal #2- "New Satellite vs old" notebook: https://github.com/rhaxx/capstone-weather/rex/forsami.ipynb

Smart Goal #3- "Document/Wiki" https://github.com/yuanzhou15/capstone-weather/wiki/Feature-Team
