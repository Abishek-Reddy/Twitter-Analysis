# Importing the libraries
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np
import collections
import wordcloud
import sklearn
from wordcloud import WordCloud, STOPWORDS
from matplotlib import rcParams

# Read the CSV file with the extracted tweets
data = pd.read_csv('tweets.csv')

# Remove null values
data = data.dropna()

# Dropping user names and location
data = data.drop(['User', 'Location'], axis=1)

# Converting all the tweets to lowercase
all_tweets = ' '.join(data['Tweet'].str.lower())

# Printing to check whether the tweets are in lowercase
#print(data)

# Creating a wordcloud
stop_words = ["https", "co", "RT", "a", "@", "i", "t", "to", "the", "and"]
wordcloud = WordCloud(stopwords=stop_words, background_color="white", max_words=500).generate(all_tweets)

# Visualization
rcParams['figure.figsize'] = 10, 20
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


