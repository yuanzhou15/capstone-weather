import numpy as np

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

