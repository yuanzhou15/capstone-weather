Spetemper 4th:

For Next Week (Sept 11th):

1. 
Setup development and ML software on CCNY's servers. 
specifically: install tensorflow 1.4, and move the datasets (Radar, Satellite) to it.
Going further, this the chosen platform we decided to run our Deep learning algorithms on.
It's powerful enough with 2 GPU's.
Success will be measured by: 
- whether pix2pix can be run on the server 
- I can replicate the work done so far from last semester on the server.
Instructions to propely run the experiments will be added (or rather modified) accordingly to the repo.


2.  
Feed all satellite bands to CGAN as separate channels (as in RGB):
Based on feedback from the very last presentation of last semester. 
This is the proper way to feed different data to a DCNN. unlike the various other things I tried so far.
Compare result to the baseline we decide on in GOAL 1.
Relevant Code will be added (code that collects matching sat bands and radar data files and save them to image files, where the sat image has different bands as RGB channels)


3. 
Figure out a good baseline model:
So far I've been comparing results of various experiments to (our) other previous results.
but based on feedback, it's necessary to have a "baseline" model as a standard to which new results should be compared.
Once we've decide on a good baseline, I'll re-run the previous things we tried against it and document them.
this includes re-evaluting the various settings of Satellite images fed to the CGAN we had last semester.


Stretch Goal:
Be able to feed multi-band images to Pix2Pix on the server.
