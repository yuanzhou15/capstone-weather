# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from visdom import Visdom
import argparse
import numpy as np
import math
import os.path
import getpass
import time
from sys import platform as _platform
from six.moves import urllib


DEFAULT_PORT = 8097
DEFAULT_HOSTNAME = "http://localhost"
parser = argparse.ArgumentParser(description='Demo arguments')
parser.add_argument('-port', metavar='port', type=int, default=DEFAULT_PORT,
                    help='port the visdom server is running on.')
parser.add_argument('-server', metavar='server', type=str,
                    default=DEFAULT_HOSTNAME,
                    help='Server address of the target to run the demo on.')
FLAGS = parser.parse_args()

try:
    viz = Visdom(port=FLAGS.port, server=FLAGS.server)

    assert viz.check_connection(timeout_seconds=3), \
        'No connection could be formed quickly'

    textwindow = viz.text('Hello World!')

    updatetextwindow = viz.text('Hello World! More text should be here')
    assert updatetextwindow is not None, 'Window was none'
    viz.text('And here it is', win=updatetextwindow, append=True)

    # text window with Callbacks
    txt = 'This is a write demo notepad. Type below. Delete clears text:<br>'
    callback_text_window = viz.text(txt)

    def type_callback(event):
        if event['event_type'] == 'KeyPress':
            curr_txt = event['pane_data']['content']
            if event['key'] == 'Enter':
                curr_txt += '<br>'
            elif event['key'] == 'Backspace':
                curr_txt = curr_txt[:-1]
            elif event['key'] == 'Delete':
                curr_txt = txt
            elif len(event['key']) == 1:
                curr_txt += event['key']
            viz.text(curr_txt, win=callback_text_window)

    viz.register_event_handler(type_callback, callback_text_window)

    # matplotlib demo:
    try:
        import matplotlib.pyplot as plt
        plt.plot([1, 23, 2, 4])
        plt.ylabel('some numbers')
        viz.matplot(plt)
    except BaseException as err:
        print('Skipped matplotlib example')
        print('Error message: ', err)

    # video demo:
    try:
        video = np.empty([256, 250, 250, 3], dtype=np.uint8)
        for n in range(256):
            video[n, :, :, :].fill(n)
        viz.video(tensor=video)

        # video demo:
        # download video from http://media.w3.org/2010/05/sintel/trailer.ogv
        video_url = 'http://media.w3.org/2010/05/sintel/trailer.ogv'
        # linux
        if _platform == "linux" or _platform == "linux2":
            videofile = '/home/%s/trailer.ogv' % getpass.getuser()
        # MAC OS X
        elif _platform == "darwin":
            videofile = '/Users/%s/trailer.ogv' % getpass.getuser()
        # download video
        urllib.request.urlretrieve(video_url, videofile)

        if os.path.isfile(videofile):
            viz.video(videofile=videofile)
    except BaseException:
        print('Skipped video example')
        
   # image demo
    viz.image(
        np.random.rand(3, 512, 256),
        opts=dict(title='Random!', caption='How random.'),
    )

    # grid of images
    viz.images(
        np.random.randn(20, 3, 64, 64),
        opts=dict(title='Random images', caption='How random.')
    )

    # scatter plots
    Y = np.random.rand(100)
    old_scatter = viz.scatter(
        X=np.random.rand(100, 2),
        Y=(Y[Y > 0] + 1.5).astype(int),
        opts=dict(
            legend=['Didnt', 'Update'],
            xtickmin=-50,
            xtickmax=50,
            xtickstep=0.5,
            ytickmin=-50,
            ytickmax=50,
            ytickstep=0.5,
            markersymbol='cross-thin-open',
        ),
    )

    viz.update_window_opts(
        win=old_scatter,
        opts=dict(
            legend=['Apples', 'Pears'],
            xtickmin=0,
            xtickmax=1,
            xtickstep=0.5,
            ytickmin=0,
            ytickmax=1,
            ytickstep=0.5,
            markersymbol='cross-thin-open',
        ),
    )

    # 3d scatterplot with custom labels and ranges
    viz.scatter(
        X=np.random.rand(100, 3),
        Y=(Y + 1.5).astype(int),
        opts=dict(
            legend=['Men', 'Women'],
            markersize=5,
            xtickmin=0,
            xtickmax=2,
            xlabel='Arbitrary',
            xtickvals=[0, 0.75, 1.6, 2],
            ytickmin=0,
            ytickmax=2,
            ytickstep=0.5,
            ztickmin=0,
            ztickmax=1,
            ztickstep=0.5,
        )
    )

    # 2D scatterplot with custom intensities (red channel)
    viz.scatter(
        X=np.random.rand(255, 2),
        Y=(np.random.rand(255) + 1.5).astype(int),
        opts=dict(
            markersize=10,
            markercolor=np.random.randint(0, 255, (2, 3,)),
        ),
    )

    # 2D scatter plot with custom colors per label:
    viz.scatter(
        X=np.random.rand(255, 2),
        Y=(np.random.randn(255) > 0) + 1,
        opts=dict(
            markersize=10,
            markercolor=np.floor(np.random.random((2, 3)) * 255),
        ),
    )

    win = viz.scatter(
        X=np.random.rand(255, 2),
        opts=dict(
            markersize=10,
            markercolor=np.random.randint(0, 255, (255, 3,)),
        ),
    )

