from keys import *

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
# consumer key, consumer secret, access token, access secret.



class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']
        print(tweet)
        return (True)

    def on_error(self, status):
        print(status)



auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["keyword"])
