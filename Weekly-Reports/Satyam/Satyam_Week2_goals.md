Satyam Sharma
9/11/2018

# Stretch Goal 1:
This week I will focus on understanding the pix2pix code and running the tensorflow code on my machine. Pixel to pixel mapping has been a strong candidate for estimating precipitation over land. However, the pix2pix have performed really well at the cost of low interpretability of its black-box representation. I will dive into the code and better understand how its architechture is set up. It is relevant as it will help me better asist my peers on suggesting changes in the model and better evaluate the evaluations.

## Smart Goal #1:

S.Specific
Perform Time series analysis of Mean Bias Error(MBE) and Root Mean Square Error(RMSE) for PIX2PIX run2 results. ("Run2" basically is the term Model team and Evalution team is using for the 2nd wave. Each "run" is the data that were manipulated in some form by changinng the channel or feature)

M. Measurable
Performing a Time analysis of errors will result in 2 linecharts for Mean Bias Error(MBE) and Root Mean Square Error(RMSE) for the year 2017. Like last week's smart goal, this will also result in a sequsence of numbers representing the perfoemnca of the estimation oacross the year.

A. Achievable
This is a doable task and does not require additional research. The module required is already written as part of the last week goal. Most of the  is finished will be mainly used in this task.

R. Relevent
run1 is the first generated prediction of radar data from pix2pix. In the past, Error matrics were only performed between two images. Line chart will allow comaprison and perfomances of metrices in realtion to different weather states of the region of interest

T. Time-bound:
The deadline for this task is anticipated to be 9/18/2018. This task should be completed witih in 1 week.




## Smart Goal 2:

S.Specific
Install CUDA and Tensorflow on my Ubuntu machine. This will further allow me to work on the code independently without dealing with restrictions imposed on school servers

M. Measaureable
On succesful completion of the task I can run atleast generate one batch of test and train set.

A. Achievable
The web has full documenataion and cook books on how to install and run Tensorflow. Sami also has expereince running Tensorflow on his machine So I can reach out to him as well.


R. Relevent
In order to run the pix2pix and train the sateliite data on radar, I will need to have the prequisite libraries installed


T. Time-bound:
The deadline for this task is anticipated to be 9/18/2018. This task should be completed witih in 1 week. It is a realistic time to get started with tensorflow.




## Smart Goal 3:
S.Specific
Read pix2pix paper: Image-to-Image Translation with Conditional Adversarial Networks
by Phillip Isola et.al.

M. Measaureable
This is something difficult to measure, as merely reading the paper is not sufficient. The goal is really to understand. 


A. Achievable
It is a 17 page paper. Intial reading convinces me that the paper does not use too much of scientific jargon. 
This as a result should make it easy to follow the logic and understand architecture of the models.

In fact of the 17 pages, only 9 pages contain the textual information. Otherwise, 4 pages of the paper are devoted to table of pictures to visualize the performance of the pix2pix. And the remaining 4 pages are used for Refrences and Appendix.   

R. Relevent
In order to play with the pix2pix code in tensorlflow, it is super crucial to understand the model to suggest meaningful changes,
as jumping straight to the code might not help.  


T. Time-bound:
The deadline for this task is anticipated to be 9/18/2018. This task should be completed witih in 2 weeks. It is a realistic time to get started with tensorflow.

 
## Goals achieved from last week
Goal #1: 
Creating python modules that would contain all the inclusive functions associated with techniques to measure and validate the estimation of precipitation.


Goal #2:
Read literature attempting to estimate precipitation and mimic their techniques for evaluation while writing the python
module for evaluation
1) PERSIANN-MSA: A Precipitation Estimation Method from Satellite-Based Multispectral Analysis
2) Evaluation of TRMM Multi-satellite Precipitation Analysis (TMPA) performance in the Central Andes region and its dependency on spatial and temporal resolution.


Goal #3: 
Performed Time series analysis of Mean Bias Error(MBE) and Root Mean Square Error(RMSE) for PIX2PIX run1 results
This would make use of the python module I wrote as part of Goal #1. The idea is visulaize how each error metric performs across the year.
