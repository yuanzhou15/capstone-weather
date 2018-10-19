#!/usr/bin/env python

"""
train/test split
args:
    -src folder: has directories A and B. Contains all data. Will be left with only train data 
    -dst folder: has directories A and B. Will contain test data 
    -num of channels in A
    -test ratio:  e.g. 20
"""

import os
import sys
from shutil import move
from random import shuffle

if __name__ == '__main__':
    if len(sys.argv) > 4:
        SRC = sys.argv[1]
        DST = sys.argv[2]
        chan = int(sys.argv[3])
        ratio = int(sys.argv[4])
    else:
        print("invalid # of args")
        sys.exit(-1)
    # validate source:
    delimsrc = ''
    if '\\' in SRC:
        delimsrc = '\\'
    elif '/' in SRC:
        delimsrc = '/'
    if delimsrc:
        SRCPATH = SRC  # ''.join(SRC.split(delimsrc)[:-1])
        if not os.path.isdir(SRCPATH):
            print('INAVLID SOURCE')
            sys.exit(0)
    # validate destination:
    delimdst = ''
    if '\\' in DST:
        delimdst = '\\'
    elif '/' in DST:
        delimdst = '/'
    if delimdst:
        DSTPATH = DST  # ''.join(DST.split(delimdst)[:-1])
        if not os.path.isdir(DSTPATH):
            print('INAVLID DESTINATION')
            sys.exit(0)
    agroups = []
    araw = sorted(list(os.listdir(SRCPATH + delimsrc + "A")))
    for i in range(0, len(araw), chan):
        agroups.append(araw[i:i+chan])
    bgroups = [[i] for i in sorted(list(os.listdir(SRCPATH + delimsrc + "B")))]
    assert (len(agroups) == len(bgroups))

    rands = list(range(len(agroups)))
    shuffle(rands)
    dstA = DSTPATH + ('' if DSTPATH[-1] ==
                      delimdst else delimdst) + "A" + delimdst
    dstB = DSTPATH + ('' if DSTPATH[-1] ==
                      delimdst else delimdst) + "B" + delimdst
    srcA = SRCPATH + ('' if SRCPATH[-1] ==
                      delimsrc else delimsrc) + "A" + delimsrc
    srcB = SRCPATH + ('' if SRCPATH[-1] ==
                      delimsrc else delimsrc) + "B" + delimsrc
    for i in rands[:int(len(rands)*ratio/100.0)]:
        for f in agroups[i]:
            # print("cp " + str(srcA + f) + " " + str(dstA + f))
            move(srcA + f, dstA + f)
        for f in bgroups[i]:
            # print("cp " + str(srcB + f) + " " + str(dstB + f))
            move(srcB + f, dstB + f)
    print("Done.")
    sys.exit(0)
