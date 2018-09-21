# arg1: root folder path
# arg2: batch size
python /home/wproj/pytorch-CycleGAN-and-pix2pix/train.py --dataroot $1 --checkpoints_dir $1/checkpoints --name weather --model pix2pix --direction AtoB --batch_size $2 --gpu_ids 0,1 --display_server http://crest-cluster-node-6

