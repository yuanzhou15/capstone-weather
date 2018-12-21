# arg1: root folder path
# arg2: batch size
# arg3: number of input channels
# arg4: number of columns to display in html/visdom (pass in channels + 2)
# todo: add loadSize, fineSize arg?
python /home/wproj/new/new2/capstone-weather/pytorch-CycleGAN-and-pix2pix/train.py --dataset_mode multichannel --input_nc $3 --output_nc 1 --dataroot $1 --checkpoints_dir $1/checkpoints --name weather --model pix2pix --direction AtoB --batch_size $2 --gpu_ids 0,1 --display_server http://crest-cluster-node-6 --loadSize 256 --fineSize 256 --display_ncols $4