# Smart and Stretch Goals

**Name:** Ambiorix Cruz Angeles
**Date:** 9/2/2018

## Stretch Goals (1-3)

1. Being able to complete one full pipeline from the Feature Team -> Algorithm Team -> Evaluation Team. To be specific, creating a "control" model for comparison between future models. The result of this effort will be shown in the groups documentation file. A table of some sort listing all the future models, including this base model, will be made to keep track of important notes from each model. This is obtainable if everyone in the group puts forth there best effort when it's their teams turn to take over the current model being produced. This is relevant to our project because if we can get into a nice routine, the rest would just be changing the inputs and getting outputs.

## S.M.A.R.T. Goals (next week)

1. Taking a look at the radar data and how to properly display it. Last semester brian said we are displaying the radar data incorrectly and that we should take a look into the function he gave us and fix the issue.

2. Paul gave us new satellite data last semester that i stored into the HDD and haven't looked at. Sami would like it if i go through the updated satellite data and try to understand why the size is a lot larger than the original data giving to us. (Perhaps it is uncropped?)

3. Getting more model data. Last semester, I ordered NAM Model Data from the NOAA website but was only able to order data that was 1800(+6HRS) UTC (2PMto8PM in EST). The satellite and radar data are 30min and hourly respectively.

Week 1- S.M.A.R.T.- Specific, Measurable, Actionable, Relevant, Timebound

### S.M.A.R.T. Goal 1.

#### S. Specific:
I will go through the raw model data, extract, and crop out 2-3 features, out of the 438, to the enclosed domain of 31N-41N and 82W-102W. Afterwards, these features will be saved as a “featurename/nam_218_yyyymmdd_utc.npy” files onto a “Feature” folder in my portable HDD. Then, the HDD will be passed to the Algorithm Team, so they can create a new model for every new feature. 

#### M. Measurable: 
The result of this effort will be shown by a jupyter notebook titled “rex/feature.ipnb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. Any features fully properly extracted will be part of a list that will go in the wiki/doc page of the github repo.

#### A. Achievable:
It is possible for me to achieve this because all the raw data is stored onto my 1 TB HDD that I got for this class. My computer at home is more than capable of doing this task in a jupyter notebook environment through anaconda navigator.

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. These several models will then be examined and evaluated based on accurately they reproduce the available radar image. This task will take the team one step further and will get everyone started for this semester.

#### T. Time-bound:
This task should be done by next Sunday. 9/3/2018

### S.M.A.R.T. Goal 2.

#### S. Specific:
I can go through all the available raw radar data, satellite data, and model data, and pick out the dates and times that match. For example, they are all from the year 2017 but are taken at different frequencies throughout the day; Satellite data is every 30 minutes, Radar data is every hour, and Model data is every 6 hours. Creating a small subset of images that all correlate within every 6 hours of the Model data might give us better results when training a model.

#### M. Measurable:
The result of this effort will be shown by a jupyter notebook titled “rex/correlate.ipnb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. This subset of data will be stored on the portable HDD of the group, as a folder titled “correlate”, for the Feature Extraction team and the Model Creation team to use.

#### A. Achievable:
It is possible for me to achieve this because all the raw data is stored onto my 1 TB HDD that I got for this class. My computer at home is more than capable of doing this task in a jupyter notebook environment through anaconda navigator. If need be, a linux virtual environment will be used inside my home computer to properly use libraries like “pygrib” to be able to read the raw data into python.

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. These several models will then be examined and evaluated based on how accurately they reproduce the available radar image. This task will take the team one step further into being able to create a base model.

#### T. Time-bound:
This task should be done by next Sunday. 9/3/2018

### S.M.A.R.T. Goal 2.

#### S. Specific:
I can work on cleaning up the github master repo by organizing readme files, the wiki page, and the documentation. This will not only extend towards what I’ve done that needs documentation, it will extend to what others have yet to post up on the repo. I’ll contact them via our facebook messenger group and ask them questions about what they would like for me to document from their notebooks.

#### M. Measurable:
The result of this effort will be shown on the groups master repo: re-organizing files, updating readmes, documenting meetings, workflow, smart goals achieved, wiki page, etc.

#### A. Achievable:
Since the semester just began, I believe I will have some free time, this week, after I go back home after my classes. This doesn’t require much computing power nor coding. It is just some tidying up.

#### R. Relevant:
Organizing our documentation, updating our readme files, and editing the wiki will help in the future in case we would like to go through old code or previous results. Our team has been lacking some documentation, so I figured that if I spare time, I could do it.

#### T. Time-bound:
This task should be done by next Sunday. 9/3/2018 This task can be repeated throughout the semester if I have finished my prior smart goals. The more organized the team is, the better.

## S.M.A.R.T. Goals (last week)

Since this is the first week of smart goals, there weren't any completed goals last week. For the sake of my grade, here are the links to where you can find relevant github code for the smart goals stated above.

Smart Goal #1- "Feature Extraction" notebook: https://github.com/rhaxx/capstone-weather/rex/feature-extract.ipynb

Smart Goal #2- "Correlating Data" 
