# Smart and Stretch Goals

**Name:** Ambiorix Cruz Angeles
**Date:** 9/10/2018

## Stretch Goals (1-3)

1. Being able to complete one full pipeline from the Feature Team -> Algorithm Team -> Evaluation Team. To be specific, creating a "control" model for comparison between future models. The result of this effort will be shown in the groups documentation file. A table of some sort listing all the future models, including this base model, will be made to keep track of important notes from each model. This is obtainable if everyone in the group puts forth there best effort when it's their teams turn to take over the current model being produced. This is relevant to our project because if we can get into a nice routine, the rest would just be changing the inputs and getting outputs.

## S.M.A.R.T. Goals (next week)

1. 

2. Paul gave us new satellite data last semester that i stored into the HDD and haven't looked at. Sami would like it if i go through the updated satellite data and try to understand why the size is a lot larger than the original data giving to us. (Perhaps it is uncropped?)

3. Getting more model data. Last semester, I ordered NAM Model Data from the NOAA website but was only able to order data that was 1800(+6HRS) UTC (2PMto8PM in EST). The satellite and radar data are 30min and hourly respectively.

Week 2- S.M.A.R.T.- Specific, Measurable, Actionable, Relevant, Timebound

### S.M.A.R.T. Goal 1.

#### S. Specific:
Taking a look at the radar data and the function given to us by Brian in order to properly display the data. Last semester it was said that the way the data is being displayed is wrong. So, the function will be looked at in order to find a bug or a better understanding on how to display the data will be found.

#### M. Measurable: 
The result of this effort will be shown by a jupyter notebook titled “rex/radar-display.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. 

#### A. Achievable:
It is possible for me to achieve this because I've been working with the model data and have seen similar data and have displayed it before. My computer at home is more than capable of doing this task in a jupyter notebook environment through anaconda navigator.

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. These several models will then be examined and evaluated based on accurately they reproduce the available radar image. This task will help us get a better understanding of the radar data, as well as, give us a better way to look at it. It may also help our model creation.

#### T. Time-bound:
This task should be done by next Sunday. 9/16/2018

### S.M.A.R.T. Goal 2.

#### S. Specific:
One of our teammates from the algorithm team, Sami, would like if i dove into the new satellite data that Paul gave us last semester and compared it to the old satellite data. Sami has been using the old data most of last semester and was wondering why the new data is much larger.

#### M. Measurable:
The result of this effort will be shown by a jupyter notebook titled “rex/new-sat-data.ipynb” in the master repo. Commits will be done as often as I can remember so the progress can be tracked on github. Any interesting finds will be documented on the notebook itself as well as on the wiki page.

#### A. Achievable:
It is possible for me to achieve this because all the raw data is stored onto my 1 TB HDD that I got for this class. My computer at home is more than capable of doing this task in a jupyter notebook environment through anaconda navigator. If need be, a linux virtual environment will be used inside my home computer to properly use libraries like “netCDF4” to be able to read the raw data into python. 

#### R. Relevant:
Our project consists of training multiple supervised learning models to accurately produce radar data with satellite images and model data as input. These several models will then be examined and evaluated based on how accurately they reproduce the available radar image. Understanding the differences between the old satellite data and the new one could help us better answer Sami's question. If the new data is uncropped, it is my job to crop it so it is over the same region as the radar data.

#### T. Time-bound:
This task should be done by next Sunday. 9/10/2018

### S.M.A.R.T. Goal 3.

#### S. Specific:
More model data is required. Currently, on the HDD, there is only daily available from 1800UTC to 2300UTC. The radar data is as frequent as every hour and the satellite data is as frequent as every 30 minutes. In order to properly make a trained model in the future, it would be better if more data that correlates existed.

#### M. Measurable:
The data will be appended to the existing data on the harddrive as well as extracted and cropped into the features that were already previously extracted.

#### A. Achievable:
All of the code for extracting and cropping has already been made. Getting the data is as easy as sending an email to NOAA with the frequency and length of the data. Within a few days they should respond with an email-link leading to a website where all the data can be downloaded

#### R. Relevant:
The more data we have, the better trained our models will be

#### T. Time-bound:
This task should be done by next Sunday. 9/10/2018 

## S.M.A.R.T. Goals (last week)

Smart Goal #1- "Feature Extraction" notebook: https://github.com/rhaxx/capstone-weather/rex/feature-extract.ipynb

Smart Goal #2- "Correlating Data" notebook: https://github.com/rhaxx/capstone-weather/rex/correlate.ipynb

Smart Goal #3- "Document/Wiki" https://github.com/yuanzhou15/capstone-weather/wiki/Feature-Team
