import re
import os
import numpy as np
import pandas as pd
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
timeline_tweets = api.home_timeline(count=50)

# HelloWorld

print(timeline_tweets[0].text)
print(timeline_tweets[1].retweet_count)

ds_tweets = api.search_tweets(q='My physical experiment -filter:retweets', tweet_mode='extended', count=100)

ds_list = []

for i in ds_tweets:
    clean_tweet = re.sub('#|https([^\s]+)|@([^\s]+)', '', i.full_text)
    analiz = TextBlob(clean_tweet)
    ds_list.append([clean_tweet, analiz.sentiment.polarity, analiz.sentiment.subjectivity])

df_tweets = pd.DataFrame(data=ds_list, columns=["Tweet", "Polarity", "Subjectivity"])

# end of sentiment

stop_w = STOPWORDS
string_tweets = str(df_tweets["Tweet"].values)
word_cloud = WordCloud(stopwords=stop_w).generate(string_tweets)

word_cloud.to_image().show()

word_cloud.to_file('word.png')
