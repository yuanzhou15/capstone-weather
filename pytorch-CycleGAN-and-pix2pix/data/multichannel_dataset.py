import os.path
import random
import torchvision.transforms as transforms
import torch
from data.base_dataset import BaseDataset
from data.image_folder import make_dataset
from random import random
from PIL import Image


class MultiChannelDataset(BaseDataset):
    @staticmethod
    def modify_commandline_options(parser, is_train):
        return parser

    def initialize(self, opt):
        self.opt = opt
        self.root = opt.dataroot
        self.dir_AB = os.path.join(opt.dataroot, opt.phase)
        self.A_paths = sorted(make_dataset(os.path.join(self.dir_AB, 'A')))
        self.B_paths = sorted(make_dataset(os.path.join(self.dir_AB, 'B')))
        # assert(opt.resize_or_crop == 'none')
        assert(self.opt.direction == 'AtoB')
        assert(self.opt.output_nc == 1)
        print('A, B counts: '+str(len(self.A_paths)) + '  ' + str(len(self.B_paths)))
        if len(self.B_paths)*self.opt.input_nc != len(self.A_paths):
            print("warning: number of A, B images don't match. Double-check image filenames!")


    def __getitem__(self, index):
        A_path = self.A_paths[index*self.opt.input_nc : (index+1)*self.opt.input_nc]
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
            Araw = Image.open(p).convert('RGB').resize((self.opt.loadSize, self.opt.loadSize), Image.BICUBIC)
            w, h = Araw.size
            assert(w == h)
            assert(w%4 == 0)
            Ai = transforms.ToTensor()(Araw)
            Ai = transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))(Ai)
            tmp = Ai[0, ...] * 0.299 + Ai[1, ...] * 0.587 + Ai[2, ...] * 0.114
            Ai = tmp.unsqueeze(0)
            # if str(Ai.size()) != 'torch.Size([1, 256, 256])':
            #     print('Wrong Ai shape: ' + str(Ai.size()))
            As.append(Ai)
        A = torch.stack(As, dim=1)[0]

        # load B
        Braw = Image.open(B_path).convert('RGB').resize((self.opt.loadSize, self.opt.loadSize), Image.BICUBIC)
        w, h = Braw.size
        assert(w == h)
        assert(w%4 == 0)
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
        # if random() < 0.5:
        
        # print('A final shape: ' + str(A.size()))
        # print('B final shape: ' + str(B.size()))
        return {'A': A, 'B': B,
                'A_paths': A_path[0], 'B_paths': B_path}

    def __len__(self):
        return len(self.B_paths)

    def name(self):
        return 'MultiChannelDataset'
