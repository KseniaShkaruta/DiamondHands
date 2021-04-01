FROM rocker/rstudio:4.0.4

#standard deps
RUN apt-get update && apt-get install -y \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    xtail \
    wget \
    libxml2 \
    libglpk-dev

# add a shiny server
# RUN export ADD=shiny && bash /etc/cont-init.d/add
# https://github.com/rocker-org/rocker-versioned/issues/219
RUN /rocker_scripts/install_shiny_server.sh

# install tidyverse
RUN install2.r tidyverse highcharter flexdashboard