Satyam Sharma
11/05/2018

## Stretch Goal #1:
With all the previous cases PNGs are being used, but that doesn't have to be the case. In fact it might in our best interest to train and test using the orignal format. Goal for this week is to use Random Forest and Linear Regression with varying window sizes on the NPY version of the datasets.

## Smart Goal #1:
S.Specific
Building a Numpy version of Random Forest for 1x1 window and 3x3 window for five Satellite only. This time also use cross-validation strategy like K-fold.

M. Measurable
Completion of this Goal will result in a jupyter notebook with tested and trained evaluation results of NPY dataset.

A. Achievable
I have already written code for PNG version, I have to carefully port it to make it to use NPY dataset.

R. Relevent
PNGs undergo lot of preprocessing that might not be relevant. Additionally, if the model performs well in the NPY version, it will be easier for the metrologist/geologist to interpret the results.
 
T. Time-bound:
Yes, the goal is achievable and feasible for completing it in 1 week. Everything is possible


## Smart Goal #2:
S.Specific
Building a Numpy version of Random Forest for 1x1 window and 3x3 window for five Satellite Bands *and* the four Model data. This time also use cross-validation strategy like K-fold.

M. Measurable
Completion of this Goal will result in a jupyter notebook with tested and trained evaluation results of NPY dataset.

A. Achievable
I have already written code for PNG version, I have to carefully port it to make it to use NPY dataset.

R. Relevent
PNGs undergo lot of preprocessing that might not be relevant. Additionally, if the model performs well in the NPY version, it will be easier for the metrologist/geologist to interpret the generated results.
 
T. Time-bound:
Yes, the goal is achievable and feasible for completing it in 1 week. Everything is possible



## Smart Goal #3:
S.Specific
Use k-Fold and Perform visualization of the image by combining the generated pixels from the different models back to the 2d array.

M. Measurable
Completion of this Goal will result in jupyter notebooks from now onwards that will now also contain actual images that were generated.

R. Relevent
So far the evaluations are performed quantitatively. i.e. using RMSE, Confusion Matrix, and Histograms. Visualing the actaul generated images will tell us if the models are actually working. and more specifically, where and where not.

A. Achievable
It is achievable. It should be silimar to reversing the process of extracting the pixels. But, I am transforming the pixels to back.

T. Time-bound:
Yes, the goal is achievable and feasible for completing it in 1 week. Everything is possible

## Goals achieved from last week
Goal #1
Changed filter from "3x3 block average" to "3x3 overlap" :  {(top-left) (top-center) (top-right) (middle-left) (middle-center) (middle-right) (bottom-left) (bottom-center) (bottom-right)} for the inputs for each of the satellite bands and the four model data.
Commit:

Goal #2:
Ran *1x1* Pixel's' to Pixel Random Forest Reregression but now with Model data {Relative Humidity, Specific Humidity, Temperature, and Visibility} included.
Commit:

Goal #3:
Ran *1x1* Pixel's' to Multiple Linear Reregression but now with Model data {Relative Humidity, Specific Humidity, Temperature, and Visibility} included.
Commit:
