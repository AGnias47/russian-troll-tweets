#!/usr/bin/env python3
#
#   A. Gnias
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.7.5
#   Vim 8.1

import utilities.data
from tweet.tweet import Tweet

data = utilities.data.read_csv_as_list_of_dicts("data/IRAhandle_tweets_13.csv")
tweets = [Tweet(tweet) for tweet in data]
print(tweets[0])
