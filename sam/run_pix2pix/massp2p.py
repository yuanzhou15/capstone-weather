#!/usr/bin/env python

import os as os
import sys
import shutil as sh
import glob
import subprocess
from itertools import chain, combinations

usage = """
Usage:
arg1:    data root directory path
arg2:    directory where combinations results will be saved
arg3:    -c produce all combinations of chosen channels. -s do a single pix2pix run on chosen channels
args...: channels

Don't use relative paths for arg1 and arg2!!!

Example: ./massp2p /path/to/dataset /path/to/dst -c 1 2 6
"""

datadir = ''
rootdir = ''

templatedir = '/home/wproj/new/template'
trainscript = '/home/wproj/new/new2/capstone-weather/sam/run_pix2pix/pytorch_train.sh'
testscript  = '/home/wproj/new/new2/capstone-weather/sam/run_pix2pix/pytorch_test.sh'

class Combination:
    def __init__(self, i, channels):
        self.decimal = i
        # self.binary = '0'
        self.channels = channels
        self.folder = rootdir + '/' + str(self.decimal)
        self.n = len(channels)  # how many channnels


def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    y = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    next(y)
    return y


def setupComb(comb):
    # create comb's dir
    subprocess.call(['cp', '-r', templatedir, comb.folder])
    print('cp -r %s %s'%(templatedir, comb.folder))
    # add description
    with open(comb.folder + '/description.txt', 'w') as f:
        f.write(str(comb.channels))

    # copy input/output channels to train/test folders as symlinks
    for f in glob.glob(datadir + '/train/A/*A%s.png'%str(x)):
        subprocess.call([
            'ln', '-s', f, comb.folder + '/train/A/'
        ])
    for f in glob.glob(datadir + '/test/A/*A%s.png'%str(x)):
        subprocess.call([
            'ln', '-s', f, comb.folder + '/test/A/'
        ])
    for f in glob.glob(datadir + '/train/B/*'):
        subprocess.call([
            'ln', '-s', f, comb.folder + '/train/B/'
        ])
    for f in glob.glob(datadir + '/test/B/*'):
        subprocess.call([
            'ln', '-s', f, comb.folder + '/test/B/'
        ])


def trainTestComb(comb):
    # train
    subprocess.call(' '.join([
        trainscript,
        comb.folder,
        '1',
        str(comb.n),
        str(comb.n + 2)]), shell=True
    )

    # test
    subprocess.call(' '.join([
        testscript,
        comb.folder,
        '1',
        str(comb.n),
    ]), shell=True)


def postComb(comb):
    # move results to comb's main directory, and delete everything else
    subprocess.call([
        'cp', '-r', comb.folder + '/checkpoints/weather/web', comb.folder + '/results_train'
    ])
    subprocess.call([
        'rm', '-r', comb.folder + '/checkpoints'
    ])
    subprocess.call([
        'cp', '-r', 'results', comb.folder + '/results_test'
    ])
    subprocess.call([
        'rm', '-r', 'results'
    ])


def runComb(comb):
    setupComb(comb)
    trainTestComb(comb)
    postComb(comb)


if __name__ == '__main__':
    if len(sys.argv) > 4:
        datadir = sys.argv[1]
        rootdir = sys.argv[2]
        allcombs = sys.argv[3] == '-c'
        channels = sys.argv[4:]
    else:
        print(usage)
        sys.exit(0)

    if not os.path.isdir(rootdir):
        subprocess.call(['mkdir', rootdir])
    if rootdir:
        if rootdir[-1] in '/\\':
            rootdir = rootdir[:-1]
    if datadir:
        if datadir[-1] in '/\\':
            datadir = datadir[:-1]

    if allcombs:
        print("Will produce %d experiments"%(2**len(channels)))
        i = 1
        for s in powerset(channels):
            print('Experiment %d/%d. Channels: %s'%(i,2**len(channels), list(s)))
            comb = Combination(i, list(s))
            i += 1
            # try:
            runComb(comb)
            # except Exception as e:
                # print(e)
    else:
        print("Will produce 1 experiment")
        comb = Combination(1, channels)
        # try:
        runComb(comb)
        # except Exception as e:
        #     print(e)

    print("All done.\n")
