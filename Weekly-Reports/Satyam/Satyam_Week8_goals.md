Satyam Sharma
10/22/2018

# Stretch Goal #1:
From the feedback received during the meeting, I will now train the random forest with larger number of input and out images but this time with *3x3* *5x5* *7x7* *9x9* window averaging block. This time I intend to train my model with 93 sets of images. That is, each set consist of the 4 sattelite 256x256 images in the png format and their 1 radar 256x256 image also in png format.

# Stretch Goal #2:
From the feedback received during the meeting, I will now train the random forest with larger number of input and out images. This time I intend to train my model with 93 sets of images. That is, each set consist of the 4 sattelite 256x256 images in the png format and their 1 radar 256x256 image also in png format.

## Smart Goal #1

### S.Specific
I will run the 1x1 Pixel's' to Pixel Random Forest Reregression on set of 93 images. This will provide with a better understanding about which features are important. 

### M. Measurable
Completion of this Goal will result in a jupyter notebook showcasing the feature importance after training 93 256x256 images 

### A. Achievable
Due to the time I had spent researching random forest and training with small amouonts of datasets, makes me preapred to deal and interpret results from larger datasets as well.

### R. Relevent
This will provide with a better understanding on which features are important. Previously, during training Random Forest with small amount of data, the feature importances were variable with different sets. Training with larger amount of data at once should account for more varied inputs and avoid overfitting problems.

### T. Time-bound:
Yes, the goal is achievable and feasible for completing it in 1 week. 



## Smart Goal #2
### S.Specific
I will run the *3x3* *5x5* *7x7* *9x9* Pixel's' to Pixel Random Forest Reregression on set of 93 images. This will provide with a better understanding about which features are important.

### M. Measurable
Completion of this Goal will result in a jupyter notebook showcasing the feature importance after training 93 256x256 images 

### A. Achievable
Due to the time I had spent researching random forest and training with small amouonts of datasets, makes me preapred to deal and interpret results from larger datasets as well.

### R. Relevent
This will provide with a better understanding on which features are important. Previously, during training Random Forest with small amount of data, the feature importances were variable with different sets. *Moreover,* using the filter i can capture account for neighboring pixels

### T. Time-bound:
Yes, the goal is achievable and feasible for completing it in 1 week. 


## Smart Goal #3
I am curious on what other ways could be used to determine the feature importance besides using the in-built random forest function. Moreover, is it possible to do as good as random Forest with something that is much simpler. Linear Regression is a good prospect for answering both of the questions. The idea is to use the magnitude of the coeffficients as analogous to feature importance. 

### S.Specific
I will use Linear Regression and train using *3x3* *5x5* *7x7* *9x9* windows to Pixel on set of 93 images. This will provide with a better understanding about which features are important.

### M. Measurable
Completion of this Goal will result in a jupyter notebook showcasing the coefficients (feature importance) after training 93 256x256 images 

### A. Achievable
Due to the time I had spent researching random forest and training with small amouonts of datasets, makes me preapred to deal and interpret results from larger datasets with window functions as well.

### R. Relevent
While Random Forest seems promising in determing what features are important. I wanted to use the magnitude of the coeffficients as analogous to feature importance and find I can confirm the same resulsts as Random Forest's feature importance function.

### T. Time-bound:
Yes, the goal is achievable and feasible for completing it in 1 week. 


## Goals achieved from last week
Goal #1:
Random forest in scikit learn in python. Implement Random Forest for 1 input/output of from the dataset (i.e. 1 image each the four bands of satellite and their 1 corresponding radar). Outcome is realizing which bands have more prominence using Feature Importance.
Commit:
https://github.com/satyamsharma/capstone-weather/commit/7ef3d6be33ede6565e87bc4ee04294e68a8dfe72


Goal #2:
Performing Sanity check and testing for the stability of the Random forest's Feature Importance by training with anoother image.
Commit:
https://github.com/satyamsharma/capstone-weather/commit/db7da722ba8484ffdcf66ca934cf7158c78f5b95
