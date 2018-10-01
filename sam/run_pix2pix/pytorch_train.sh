# arg1: root folder path
# arg2: batch size
# arg3: number of input channels
# todo: add loadSize, fineSize arg?
python ~/pytorch-CycleGAN-and-pix2pix/train.py --dataset_mode multichannel --input_nc $3 --output_nc 1 --dataroot $1 --checkpoints_dir $1/checkpoints --name weather --model pix2pix --direction AtoB --batch_size $2 --gpu_ids 0,1 --display_server http://crest-cluster-node-6 --loadSize 256 --fineSize 256

