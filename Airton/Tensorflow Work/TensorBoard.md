#  TensorBoard Connection

## Connecting

In order to connect to the tensorboard we a writer that will submit the info to the tensorboard

Code example:<br/>
file_writer = tf.summary.FileWriter('/path/to/logs', sess.graph)<br/>

Once you have event files that have been written you can start running TensorBoard and provide the log directory to which the writer is written to<br/>

Code:<br/>
tensorboard --logdir path/to/logs<br/>
The logdir is path/to/logs which can be seen on the FileWriter code

## TensorBoard Images

Below you can see te graphs that can be created using data from the network that is run, which can be useful to detect information like errors.<br/>

<img src="othertrial.png" width="800"><br/> 

img src="AandCE.png" width="800"><br/> 

img src="layer1a.png" width="800"><br/> 

img src="layer1b.png" width="800"><br/> 
