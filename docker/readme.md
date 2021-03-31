# TODO
* make a directory that will have R code/dashboards for visualization
    - this can be mounted to the container so our dashboard code will be in version control
* create some helloworld dashboard examples
* python3 comes installed from teh OS - maybe install miniconda incase we need more flexibility/package management?
* once the image is more complete, publish it to dockerhub so users can install from there instead of running locally

# Overview

This docker image starts from an ubuntu 18.04 image with rstudio server installed. It adds other dependencies for installing other software, installs shiny server, and installs the tidyverse packge.

It can be used to easily share an environment that's used for dashboards/data visualization.


# Building the container

## Build locally from dockerfile

This builds the image from the dockerfile
* `docker build -t name-for-your-image .`

## Install a published image
* **TODO**

# Running
Then you can run the image
```
docker run -d \
> -p 1234:3838 \
> -p 3423:8787 \
> -e PASSWORD=mypwd
> name-for-your-image
```
* the output will give you a docker containerid. Or use `docker ps` to see running contianers
    - you can go to the shell of the running container by running `docker exec -it <<<CONATINERID>>> bash`
* the ports can be changed, 1234 will have the shiny server - http://localhost:3423/
* 3423 will have the rstudio server (IDE)


# Using the evironment
* Go to `http://localhost:3423/` to go to the Rstudio IDE. It can be used to access the OS via terminal too
* Go to `http://localhost:1234/` to go to the shiny server - there's some examples right now such as: http://localhost:1234/01_hello/
    - Some included sample apps: `01_hello,02_text,03_reactivity,04_mpg,05_sliders,06_tabsets,07_widgets,08_html,09_upload,10_download,11_timer `


