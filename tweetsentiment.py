import tweepy
import csv
from textblob import TextBlob

# Step 1 authenticate

consumer_key = '####'
consumer_secret = '####'

access_token='####'
access_token_secret='####'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 2 retrieve tweets

public_tweets = api.search('')




# Step 3 creat csv file and write tweets into file along with polarity
with open('tweets.csv', 'w') as csv_file:
    fieldnames = ['Tweet', 'Sentiment']
    tweet_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')

    tweet_writer.writeheader()

# Step 4 Perform Sentiment Analysis on Tweets
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
            tweet_writer.writerow({'Tweet': tweet.text, 'Sentiment': 'Positive'})
        else:
            tweet_writer.writerow({'Tweet': tweet.text, 'Sentiment': 'Negative'})
