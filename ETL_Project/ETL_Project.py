# DS 3002 Data Project 1
# Author: Josephine Johannes
import pandas as pd
# from kaggle.api.kaggle_api_extended import KaggleApi

# Retrieve a remote data file by URL
''' I found out how to download a file using the Kaggle API and got it to work but thought it would be too complicated
 to download because it requires that you install it using 'pip install kaggle' and you have to generate a specific 
 API token from Kaggle which downloads a kaggle.json file, and then you have to place it in the right directory which is 
 C:/User/(your-username)/.kaggle/. So I thought I'd leave the Kaggle code here for fun :)
 
csv_url = 'https://www.kaggle.com/thespacefreak/taylor-swift-spotify-data?select=spotify_taylorswift.csv'
# Used link to get Taylor Swift's spotify data 
api = KaggleApi()
api.authenticate()
api.dataset_download_file('thespacefreak/taylor-swift-spotify-data', 'spotify_taylorswift.csv')

data = pd.read_csv('spotify_taylorswift.csv')
print(data)
'''
# 1. Ingest a local file mounted from the GitHub and the data was taken from Kaggle
# using the pandas library automatically changes the format from CSV to a dataframe
data = pd.read_csv('spotify_taylorswift.csv')

# 3. Modify the number of columns from the source to the destination
# Removed the artist column because it's Taylor Swift's data
mod_data = data.drop(['artist'], axis=1)
print(mod_data)
# Use the .to_json() function from pandas to convert from a dataframe to JSON
# the .to_json() file also writes the file to the folder
# 2. Convert from CSV to JSON
# 3. # Converted file should be written to disk, or pushed to S3, or written to a SQL database
data_json = mod_data.to_json('./taylorswift.json', orient='index')

# BONUS: Use an API to pull information realtime
'''
s3 = boto3.resource('s3')
s3object = s3.Object('jj4emproject')
'''

# Generate a brief summary of data file ingestion including
# Number of Records
print("The number of records for Taylor Swift's spotify data is "+ str(len(mod_data)) + " records")
# Number of Columns
num_columns = str(len(list(mod_data.columns.values)))
print("The number of columns in the data are " + num_columns + " columns")

# Processor should produce informative errors should it be unable to complete operation
# Exception handling