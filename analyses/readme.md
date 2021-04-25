# Overview
The analysis directory contains the python scripts and Jupyter notebooks which we've used for the data wrangling and analysis activities described in our report. The approximate "order" of the activities were:

# Data
Data is available in S3

https://dva-sp2021-team38.s3.amazonaws.com/public/exported_stock_data.csv
https://dva-sp2021-team38.s3.amazonaws.com/public/raw_reddit_pull.zip
https://dva-sp2021-team38.s3.amazonaws.com/public/posts_with_scores.csv
https://dva-sp2021-team38.s3.amazonaws.com/public/posts_with_scores_and_ticker.csv

# Scripts
* wsb_data_pull.py
    - This script was used to pull raw data from the r/WallStreetBets Reddit.The script can be further edited to specify post and comments from other subreddits or specific authors. Additionally, user's are able to change the fields collected to suit their specific research efforts.
* initial_data_cleaning.ipynb
    - This notebook uses pyspark to filter the output from the first data pull to remove unusable data that would add noise to our analysis.
* vader_sentiment_analysis.ipynb
    - This notebook uses the vaderSenitment library to perform sentiment scoring on the cleaned data.
* wsb_ticker_tagging.ipynb
    - This notebook tags the Reddit data with what stocks are mentioned in the text.
* cross_correlation_analysis.ipynb
    - This notebook explores the data to find any correlation and causal relationships between Reddit sentiment and sock data. First, data is prepared for the analysis and calculations . Next data is visualized in graphs to spot any obvious patterns. Next, correlation metrics are created for different data series combinations. Finally, Spearman and cross-correlations are calculated

