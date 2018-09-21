#!/bin/bash
# argument 1: path to root folder
python /home/wproj/capstone-weather/pix2pix/tools/process.py --input_dir $1/A --b_dir $1/B --operation combine --output_dir $1/combined
echo "done step1"
python /home/wproj/capstone-weather/pix2pix/tools/split.py --dir $1/combined
echo "done!"
