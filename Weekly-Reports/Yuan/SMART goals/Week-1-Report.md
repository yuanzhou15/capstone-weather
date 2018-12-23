## Week one report

### SMART goal 1
##### This goal was completed as I moved Radar data and one band of the satellite data onto the machines in the basements. Together the data took up about 11G, and this does not include the rest of the bands from satellite, and the model data. There is data on the machines that can be used now. The data was moved using rsync at the linux lab, although it was hard to figure out, the process of moving the data from a hard drive to the machine took a really long time. The next step is to minimize the model data to only data that we need, so that we don't irrelevant data take up the space. After extracting only the neccessary information, we would then move only those features to the node. 

### SMART goal 2
##### This goal was completed as I did document on the linear regression model, and added neccessary comments to the model from reformatting data to plugging it into the model. This can be seen in my linear regression Jupyter Notebook. The next step would be to plug in model data into the linear regression model to improve the results, and running the model on more data, hopefully this will be done on the nodes since my personal laptop cannot hold satellite, radar and model all at the same time.

### SMART goal 3
#### This goal was also completed as I was able to get the data on to my personal laptop. The data comes in multiple sets, 1 hourly, 3 hourly, 6 hourly, Daily, Monthly, and Yearly. I have been using the hourly data since it's the closest to half hourly, and 15 increments of the radar and satellite data. Further step would be to visualize the PERSIANN data which I also completed.

### SMART goal 4
##### The last goal of the week was done using a combination of matplotlib and basemap. The coverage of the data is from lat: -60 - 60 long: 0 -360. The units of data is mm rain accumulation for 1 hour. This range of data does not match the range of data given by the satellite data and radar data. So if I choose to continue with the PERSIANN model, I would wish to edit the range to match the range of the satellite and radar data. 
