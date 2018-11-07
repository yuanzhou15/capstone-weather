Satyam Sharma
10/30/2018

## Smart Goal #1:
As suggested in the meeting, I will have to replace the average block filter to true window pixels and expand my input features with {(top-left) (top-center) (top-right) (middle-left) (middle-center) (middle-right) (bottom-left) (bottom-center) (bottom-right)} for each of the satellite bands and the four model data

S.Specific
I will incorporate the the three window sampling in the random forest and linear regression.

M. Measurable
Completion of this Goal will result in a jupyter notebook showcasing the feature importance with Satellite and Model Data

A. Achievable
Due to the time I had spent researching random forest and training with small amouonts of datasets, makes me preapred to deal and interpret results from larger datasets as well.

R. Relevent
it will us tell which neighborhood pixels are more prominent surrounding a pixel. This also will provide with a better understanding on which features are important in both satellit and in Model data. 

T. Time-bound:
Yes, the goal is achievable and feasible for completing it in 1 week. 

## Smart Goal #2:
I have to reinvent my workflow to now also include Model data as well namely: Relative Humidity, Specific Humidity, Temperature, and Visibility and also perform 1x1 and 3x3 window overlapping sampling.

S.Specific
I will run the 1x1 Pixel's' to Pixel Random Forest Reregression on set of 93 images. This will provide with a better understanding about which features are important. 

M. Measurable
Completion of this Goal will result in a jupyter notebook showcasing the feature importance with Satellite and Model Data with 3x3 *overlapping* window

A. Achievable
Due to the time I had spent researching random forest and training with small amouonts of datasets, makes me preapred to deal and interpret results from larger datasets as well.

R. Relevent
This will provide with a better understanding on which features are important in both satellit and in Model data. 

T. Time-bound:
Yes, the goal is achievable and feasible for completing it in 1 week.

## Smart Goal #3:
Do the exact same thing did in Goals 1 and 2 now using Multiple Linear Regression. That is include overlapping of the pixels during inputting the dataset and include Model Data.


## Goals achieved from last week
Goal #1:
ran the *1x1* Pixel's' to Pixel Random Forest Reregression on set of 93 set of images.  That is, each set consist of the 5 sattelite 256x256 images in the png format and their 1 radar 256x256 image also in png format.
Commit:
https://github.com/satyamsharma/capstone-weather/commit/5814d76eb9b9b13513fca47743675f56c28b5781

Goal #2:
ran the *3x3* *5x5* *7x7* *9x9* Pixel's' to Pixel Random Forest Reregression on set of 93 set of images. That is, each set consist of the 4 sattelite 256x256 images in the png format and their 1 radar 256x256 image also in png format.
Commit:
https://github.com/satyamsharma/capstone-weather/commit/cbaa705dfcccd3bbce2d703e58b6127b070c333e
https://github.com/satyamsharma/capstone-weather/commit/acd12236546452ef1b6e157a3d7e1b24bb716cf0
https://github.com/satyamsharma/capstone-weather/commit/f94ee2d539f3067f3d03294b6b5e05078705e371
https://github.com/satyamsharma/capstone-weather/commit/b710333c593d9542037bb648f78ba4e1b326a54e

Goal #3:
ran the *1x1* *3x3* *5x5* *7x7* *9x9* Pixel's' to Pixel *Linear* Regression on set of 93 set of images. That is, each set consist of the 4 sattelite 256x256 images in the png format and their 1 radar 256x256 image also in png format.
Commit:
https://github.com/satyamsharma/capstone-weather/commit/f9d7e86a6c28262185954f39cd846d312020f82a
https://github.com/satyamsharma/capstone-weather/commit/9e2c97f4f2eee5b4eed894758a649f068d2b9131
https://github.com/satyamsharma/capstone-weather/commit/3653e3fddea3779a0f5365aef1268a37868bc5c0
https://github.com/satyamsharma/capstone-weather/commit/e89c379f2c53efc3db49c7bfa646ce33b8f33110
https://github.com/satyamsharma/capstone-weather/commit/92eecf5814e63f7c699568b2f27f90cf4629ec7f
