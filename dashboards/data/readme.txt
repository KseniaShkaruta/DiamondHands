***DO NOT DELETE THIS DIRECTORY**

Files for dashboards will be stored here when the dashboards directory is mounted to the docker container with Shiny Server. 
The dashboards will automatically detect if the needed file is present here and if not, download from S3, and place it in this data directory for usage. Files stored here won't be pushed to the repository but the directory structure is needed for dashboards to function properly.
