#!/usr/bin/env python3
#
#   A. Gnias
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.7.5
#   Vim 8.1

import utilities.data
from tweet.tweet import Tweet
from collections import Counter
import matplotlib.pyplot as plt

data = utilities.data.read_csv_as_list_of_dicts("data/IRAhandle_tweets_13.csv")
tweets = [Tweet(tweet) for tweet in data]
print(tweets[0])

languages = Counter([t.language for t in tweets])
print(f"Total languages used: {len(languages.keys())}")

most_common_languages = languages.most_common(5)
language, count = zip(*most_common_languages)
plt.bar(language, count)
plt.show()
