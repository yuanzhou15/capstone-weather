import numpy as np
from PIL import Image

from sklearn.metrics import confusion_matrix
import scikitplot as skplt

import matplotlib as plt
%matplotlib inline

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray;

def rgb2red(rgb):
    return rgb[:,:,0]

def rgb2green(rgb):
    return rgb[:,:,1]

def rgb2blue(rgb):
    return rgb[:,:,2]
    
def viewImage(img_link):
    Image.open(img_link).show()


def rmse(prediction, target):
    return np.sqrt(((prediction - target) ** 2).mean());


def mbe(prediction, target):
    return np.sum(target - prediction)/np.sum(target) * 100;


def cv_rmse(prediction, target):
    return (rmse(prediction, target)/(np.sum(target)/np.prod(prediction.shape)))*100;


def rmse_dir(prediction_dir, target_dir, channel='gray'):
    if channel=='r':
        prediction = rgb2red(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    elif channel=='g':
        prediction = rgb2green(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    elif channel=='b':
        prediction = rgb2blue(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    else:
        prediction = rgb2gray(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
        
    return rmse(prediction, target);



def mbe_dir(prediction_dir, target_dir, channel='gray'):
    if channel=='r':
        prediction = rgb2red(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    elif channel=='g':
        prediction = rgb2green(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    elif channel=='b':
        prediction = rgb2blue(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    else:
        prediction = rgb2gray(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
        
    return mbe(prediction, target);


def cv_rmse_dir(prediction_dir, target_dir, channel='gray'):
    if channel=='r':
        prediction = rgb2red(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    elif channel=='g':
        prediction = rgb2green(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    elif channel=='b':
        prediction = rgb2blue(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
    else:
        prediction = rgb2gray(np.array(Image.open(prediction_dir)));
        target = rgb2gray(np.array(Image.open(target_dir)));
        
    return cv_rmse(prediction, target);

def confusionMatrix_regression (y_true, y_pred, threshold, isNormalized=True):
    y_true_copy = np.copy(y_true)
    y_pred_copy = np.copy(y_true)
    
    y_true_copy[y_true_copy <= threshold] = 0
    y_true_copy[y_true_copy > threshold] = 1
    
    y_pred_copy[y_true_copy <= threshold] = 0
    y_pred_copy[y_true_copy > threshold] = 1
    
    skplt.metrics.plot_confusion_matrix(y_true_copy, y_pred_copy, normalize=isNormalized)
    plt.show()


