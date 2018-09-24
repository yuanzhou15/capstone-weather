import os.path
import random
import torchvision.transforms as transforms
import torch
from data.base_dataset import BaseDataset
from data.image_folder import make_dataset
from PIL import Image


class MultiChannelDataset(BaseDataset):
    @staticmethod
    def modify_commandline_options(parser, is_train):
        return parser

    def initialize(self, opt):
        self.opt = opt
        self.root = opt.dataroot
        self.dir_AB = os.path.join(opt.dataroot, opt.phase)
        self.A_paths = sorted(make_dataset(self.dir_AB))
        self.B_paths = sorted(make_dataset(self.dir_AB)) 
        assert(opt.resize_or_crop == 'none')
        assert(self.opt.direction == 'AtoB')
        assert(self.opt.output_nc == 1)
        if len(B_paths)*self.opt.input_nc != len(A_paths):
            print("warning: number of A, B images don't match. Double-check image filenames!")


    def __getitem__(self, index):
        A_path = self.A_paths[index*self.opt.input_nc : index*(self.opt.input_nc+1)]
        B_path = self.B_paths[index]
        
        # if self.opt.direction == 'BtoA':
        #     input_nc = self.opt.output_nc
        #     output_nc = self.opt.input_nc
        # else:
        #     input_nc = self.opt.input_nc
        #     output_nc = self.opt.output_nc

        # load all A channels
        As = []
        for p in A_path:
            # each image is 8-bit channel
            Araw = Image.open(p).convert('RGB')
            w, h = Araw.size
            assert(w == h)
            assert(w//4 == 0)
            Ai = transforms.ToTensor()(Araw)
            Ai = transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(Ai)
            tmp = Ai[0, ...] * 0.299 + Ai[1, ...] * 0.587 + Ai[2, ...] * 0.114
            Ai = tmp.unsqueeze(0)
            As.append(Ai)
        A = torch.stack(As, dim=2)

        # load B
        assert (out)
        Braw = Image.open(B_path).convert('RGB')
        w, h = Braw.size
        assert(w == h)
        assert(w//4 == 0)
        B = transforms.ToTensor()(Braw)
        B = transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(B)
        tmp = B[0, ...] * 0.299 + B[1, ...] * 0.587 + B[2, ...] * 0.114
        B = tmp.unsqueeze(0)

        # if (not self.opt.no_flip) and random.random() < 0.5:
        #     # todo: what's this?
        #     idx = [i for i in range(A.size(2) - 1, -1, -1)]
        #     idx = torch.LongTensor(idx)
        #     A = A.index_select(2, idx)
        #     B = B.index_select(2, idx)


        return {'A': A, 'B': B,
                'A_paths': A_paths[0], 'B_paths': B_path}

    def __len__(self):
        return len(self.A_paths)

    def name(self):
        return 'AlignedDataset'
