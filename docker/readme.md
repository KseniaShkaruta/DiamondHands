
# Overview

This docker image starts from an ubuntu 18.04 image with rstudio server installed. It adds other dependencies for installing other software, installs shiny server, and installs the tidyverse packge.

It can be used to easily share an environment that's used for dashboards/data visualization.


# Building the container

## Build locally from dockerfile

This builds the image from the dockerfile. Run this from the directory where the dockerfile is  (or change `.` to `./path/to/Dockerfile`)
* `docker build -t name-for-your-image .`
** You may need to authenticate if you get a rate limit error - https://www.docker.com/increase-rate-limits


# Running
Then you can run the image
```
docker run -d \
-p 3333:3838 \
-p 4444:8787 \
-v ${PWD}/dashboards:/srv/shiny-server/apps \
-e PASSWORD=mypwd
name-for-your-image
```
* the output will give you a docker containerid. Or use `docker ps` to see running contianers
    - you can go to the shell of the running container by running `docker exec -it <<<CONATINERID>>> bash`
* The ports can be changed, but in the command above 3333 will have the shiny server - http://localhost:3333/
    - 4444 will have the rstudio server (IDE)


# Using the evironment
* Go to `http://localhost:4444/` to go to the Rstudio IDE. It can be used to access the OS via terminal too
    - the username is `rstudio` and password is what you set above `mypwd` in the example command
* Go to `http://localhost:3333/` to go to the shiny server - there's some examples right now such as: http://localhost:3333/01_hello/
    - Some included sample apps: `01_hello,02_text,03_reactivity,04_mpg,05_sliders,06_tabsets,07_widgets,08_html,09_upload,10_download,11_timer `


# Viewing Dashboards
* dashboards are stored in the `dashboards` directory which is mounted to the `apps` directory in the shiny server
* `http://localhost:3333/apps/name.Rmd`
