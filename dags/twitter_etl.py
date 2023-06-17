import tweepy
import os
import json
from airflow.models import Variable

# load_dotenv()
def run_twitter_etl():
    access_key = Variable.get("access_key")
    access_secret = Variable.get("access_secret")
    consumer_key = Variable.get("consumer_key")
    consumer_secret = Variable.get("consumer_secret")
    
    print("RUNNING")
    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # Creating an API object
    api = tweepy.API(auth)

    tweets = api.user_timeline(
        screen_name='@elonmusk',
        count=200,
        include_rts=False,
        tweet_mode='extended'
    )

    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": str(tweet.created_at)
        }

        tweet_list.append(refined_tweet)
    
    with open("output.json", "w") as f:
        print(tweet_list)
        f.write(json.dumps(tweet_list))

def count_favorite():
    with open("output.json", "r") as f:
        tweets = json.loads(f.read())

    tweet_counts = [tweet["favorite_count"] for tweet in tweets]
    return sum(tweet_counts)


# If you want to run directy without airflow just uncomment the functions bellow,
# Run them separately, 1 then 2.
# Dont forget to put your keys and secrets in lines 8 to 11
# 1. run_twitter_etl()
# 2. count_favorite()


