CSE 6262 Data Visualization and Analytics, Spring 2021, Team 39 - DiamondHands

########################
##### DESCRIPTION ######
########################

This package contains the code/resources for team DiamondHands' project "Did WallStreetBets Move the Market?". The main intention of our project was to determine if the sentiment on the Reddit sub-forum r/WallStreetBets is correlated to the stock market. The motivation behind this was the short squeeze of Gamestop (GME) in January 2021 which caused much controversy. It is widely believed that the driving force behind the stock rally was the
Reddit sub-forum r/WallStreetBets.

The resources here can be used to either reproduce the results we've described in further detail in our poster/final paper. We've also made it so the environments used in our project can be reproduced so individuals or other teams may look to continue the work if interested.

There are essentially 3 components to our project that has been encompassed in this package
	1. Data Retrieval, Cleansing, and Analysis
	2. Environment for Visualization
	3. Dashboarding/Data Visualization.
In the section below, we provide concise instructions on how to simply setup and run each of these components. In-depth details are in READMEs in the individual directories.




####################################
##### INSTALLATON & EXECUTION ######
####################################

All these Steps refer to the content in the "CODE" directory of our submission.

*******1. DATA RETREIVAL, CLEANSING, AND ANALYSIS*****
This refers to the "analyses" directory. Note that if the data inputs are needed, they can be downloaded from S3 as detailed in the README.md

* The directory includes a requirements.txt file and a environment.yml which can be used to reproduce our analysis environment with python virtual environment or Anaconda, respectively. Note the environment should use python 3.7
	* From the analysis directory run
		* With anaconda: `conda env create -f environment.yml`
		* With pip: `pip install -r requirements.txt`
* Activate the environment then run `jupyter-lab`
* Jupyter lab should open in your browser. From here, you can view/run the notebooks and the python script as needed
	

*****2. ENVIRONMENT FOR VISUALIZATION*****
This refers to the "docker" directory. We've created a containerized environment for hosting/developing our R Shiny based dashboards.

* A prerequisite is having docker installed: https://www.docker.com/
* From the "docker" directory, run `docker build -t some-image-name .` to create an image.
	* "some-image-name" can be changed, but make note of it for step 3


*****3. DASHBOARING/DATA VISUALIZATION*****
From the package ROOT DIRECTORY (where the analyses, dashboards, and docker directories are) run the command:

```
docker run -d \
	-p 3333:3838 \
	-p 4444:8787 \
	-v ${PWD}/dashboards:/srv/shiny-server/apps \
	-e PASSWORD=mypwd \
	some-image-name
```
* NOTE IT'S VERY IMPORTANT to be in the package root to mount the "dashboards" directory properly (line 4 in the command)
* make sure "some-image-name" is what you set in #2 above
* The "3333" and "4444" above are ports. They can be changed to any available port where you are running this.
* Line 5 sets the Rstudio server password. Change if desired.


########################
#### RUNNING A DEMO ####
########################
* If steps 2 and 3 were done above, go to http://localhost:3333/apps/diamondHandsDemo.Rmd in your browser

***DASHBOARD LOAD TIME***
The very first time you load the dashboard, it will see a needed data file is not present in "dashboards/data" and have R download the file there. This gives you a longer load time.
It may be faster to download the file yourself from https://dva-sp2021-team38.s3.amazonaws.com/public/posts_with_scores_and_ticker.csv and place it in that "dashboards/data" folder

* To access Rstudio server for developing, go to  http://localhost:4444 and login with username: rstudio, password: mypwd



########################
###### DEMO VIDEO ######
########################
https://youtu.be/g93MJ0wRnv0