Satyam Sharma
9/21/2018


#Stretch Goal 1:
This week I will focus on understanding and running the tensorflow on my machine. The pix2pix and like model have performed really well. I will dive into the code and better understand how its architechture is set up. It is relevant as it will help me better asist my peers on suggesting changes in the model and better evaluate the evaluations. (similar to last week's)


## Smart Goal #1:
S.Specific
Use tensorflow to build some of the traditional models. For this week I will build a linear regression and K-means model using tensorflow.

M. Measurable
Completion of this Goal will result in 2 runnable jupyter notebook. One notebook showcasing linear regression and another showcasing K-means.

A. Achievable
I have specifically chosen linear regression and K-means as I have already built or atleast know how to build these models. Building these models is good practice to transfer skills from keras/scipy to tensorflow.

R. Relevent
This activity is a pre-requiste in performing in tweaking pix2pix and potentially making it perform better for out use case. There are several off the shelf models that we might try and evaluate, thus it is a good idea to understand the intricacy of these models by first understanding the framework they are using: tensorflow.

T. Time-bound:
Yes, the goal is achievable and feasible for completing in 1 week. 


## Smart Goal #2:
S.Specific
Explore other approaches to evaluate model and generated images. Add ROC Curve and Confusion Matrix in the python module.

M. Measurable
This will result in two functions. One function that outputs an ROC curve and another a Confusion matrix that evaluates genrated radar vs ground truth.

A. Achievable
I have already have used ROC Curve and Confusion matrix before. And more importantly, I will be revisiting the DataCamp courses, so it will allow me to write the functions easily. I plan to pass in a threshold as a parameter for ROC Curve as ROC curve meant for binary classification. If the intensity of the pixel is greater than the threshold, then it mean it rained, otherwise it did not.

R. Relevent
Though this task doesn not directly associate with the stretch goal, addition of these two function relates of the greater task of the evaluation team.

T. Time-bound:
Yes, the goal is achievable and feasible for completing in 1 week. 


## Smart Goal #3:
S.Specific
Review Datacamp videos. Recomplete Supervised Learning in Python, Unsupervised Learning in Python, and Deep Learning in Python using keras. I felt the need to revisit all the machine learning concepts before continuing to code. This would allow me to be comprehensive when investigating the pix2pix model and ultimately code with confidence. 

M. Measurable
Though the Datacamp offers completion statistics, I had already taken the courses last semster and the completion stats from this semster might not stored. But, I will take *hand-written* notes of each and every video and coding exercise and upload it as a pdf as a proof of completion. 

A. Achievable
Each of the aforementioned course is designed to take 4-5 hrs to complete. The goal is to finish the three course. It is supposed take 12hrs to 15 hrs. Because I had already finished the courses, I should be able to finish them in significantly lesser amount of time.

R. Relevent
This activity is a pre-requiste in performing in tweaking pix2pix and potentially making it perform better for out use case. There are several off the shelf models that we might try and evaluate, thus it is a good idea to understand the intricacy of these models and potentially sort the best techniques for our use case. 

T. Time-bound:
Yes, the goal is achievable and feasible for completing in 1 week. 


## Goals achieved from last week
Goal #1:
Perform Time series analysis of Mean Bias Error(MBE) and Root Mean Square Error(RMSE) for PIX2PIX run2 results. ("Run2" basically is the term Model team and Evalution team is using for the 2nd wave. Here, run2 is differnt from run1 due the processed radar images that Rex proposed. Sami trained the model, I evaluated the images just like run1. I also reformatted evaluation report's structure in jupyter-notebook by making it cleaner and by adding more visuals.
Proof (file): https://github.com/satyamsharma/capstone-weather/blob/master/satyam/run2_evaluation.ipynb
Commit: https://github.com/satyamsharma/capstone-weather/commit/2ae59757a907ac09f206c6f079cd5d9d407fe2b8#diff-67d6da6981a8c0fa34c1a99a395b331b

Goal #2:
Installed CUDA and Tensorflow on my Ubuntu machine. This will further allow me to work on the code independently without dealing with restrictions imposed on school servers. Got access to tensorboard files generated in run1 and run2.
Proof_1 (cuda compatible videocard driver): https://github.com/satyamsharma/capstone-weather/blob/master/satyam/proofs/nvidia_videocard_installed.png
https://github.com/satyamsharma/capstone-weather/commit/9f24405f67760ebb72b3193b2bb2725c12fb5bac
Proof_2 (cuda installed): https://github.com/satyamsharma/capstone-weather/blob/master/satyam/proofs/cuda_installed.png
https://github.com/satyamsharma/capstone-weather/commit/3bfc1ee736d010b150b4aa5523103957ccfe5855
Proof_3 (tensorflow): https://github.com/satyamsharma/capstone-weather/blob/master/satyam/proofs/tensorflow_installed.png
https://github.com/satyamsharma/capstone-weather/commit/2c7bf300b64a13ea597e62ca7707ae29640556cf

Goal #3:
Read pix2pix paper: Image-to-Image Translation with Conditional Adversarial Networks by Phillip Isola et.al.
Proof (URL to pdf with my highlights/annotations):  https://drive.google.com/file/d/1RWV4ncH7qzq7FPzIsmPvbkofsdNLEF8U/view?usp=sharing

