# arg1: root folder path
# arg2: batch size
# arg3: number of input channels
# todo: add loadSize, fineSize arg?
python /home/wproj/new/new2/capstone-weather/pytorch-CycleGAN-and-pix2pix/test.py --dataset_mode multichannel --checkpoints_dir $1/checkpoints --input_nc $3 --output_nc 1 --dataroot $1 --name weather --model pix2pix --direction AtoB --batch_size $2 --gpu_ids 0,1 --loadSize 256 --fineSize 256
