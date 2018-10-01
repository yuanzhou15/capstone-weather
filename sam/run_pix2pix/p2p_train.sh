#!/bin/bash
# argument 1: path to root folder
# argument 2: num of epochs
# argument 3: batch size
python /home/wproj/capstone-weather/pix2pix/pix2pix.py --mode train --output_dir $1/train_out --max_epochs $2 --batch_size $3 --input_dir $1/combined/train --which_direction AtoB --display_freq 200
