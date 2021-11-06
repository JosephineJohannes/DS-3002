# DS 3002 Data Project 1
# Author: Josephine Johannes
import csv
import requests
import urllib.request
import pandas as pd
# Retrieve a remote data file by URL
csv_url = 'https://www.kaggle.com/thespacefreak/taylor-swift-spotify-data?select=spotify_taylorswift.csv'
# Used link to determine white wine quality
df = pd.read_csv(csv_url)
print(df)

#data = csv.reader(decode_link.splitlines(), delimiter=',')
#my_list = list(data)
#for row in my_list:
 #   print(row)
# Convert general format and data structure of the data source
# BONUS: Use an API to pull information realtime

# Modify the number of columns from the source to the destination
# ex. reducing or adding columns

# Converted file should be written to disk, or pushed to S3, or written to a SQL database

# Generate a brief summary of data file ingestion including
# Number of Records
# Number of Columns

# Processor should produce informative errors should it be unable to complete operation
# Exception handling