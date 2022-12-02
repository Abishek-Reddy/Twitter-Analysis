# Importing libraries
import tweepy
import configparser
import pandas as pd
from collections import Counter 

# Read the configs
config = configparser.ConfigParser()
config.read('config.ini')

# Reading the keys
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

# Searching for tweets with a specific keyword and geo location
keywords = ""
limit = 1000
tweets = tweepy.Cursor(api.search_tweets, q = keywords, tweet_mode = 'extended',lang="",geocode="").items(limit)

# Creating a dataframe for the extracted tweets
columns = ['User', 'Tweet', 'Location']
data = []
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text, tweet.user.location])
df = pd.DataFrame(data, columns = columns)
#print(df)

# DataFrame is being converted to a csv file
df.to_csv('tweets.csv')



# Display the word frequency
count_list = df['Tweet'].tolist()
# print(count_list)

# Function to convert
def listToString(s):

    # initialize an empty string
    str1 = """ """

    # return string
    return (str1.join(s))

# Driver code
s = count_list
count_string = listToString(s)


split_it = count_string.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(20)
print(most_occur)

