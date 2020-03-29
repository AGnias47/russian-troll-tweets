#!/usr/bin/env python3
#
#   A. Gnias
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.7.5
#   Vim 8.1

import os
import utilities.data
from tweet.tweet import Tweet
from collections import Counter
import matplotlib.pyplot as plt

# Define globals
test = True  # Set true to limit data read, set false to read all available data
test_files_to_read = 4
if test:
    print(f"Reading limited amout of data for testing; reading {test_files_to_read} files")

# Read in the data
data = list()
for i, f in enumerate(os.listdir("data")):
    print(f"Reading {f}")
    data += utilities.data.read_csv_as_list_of_dicts("data/" + f)
    if test:
        if i >= (test_files_to_read - 1):
            break

# Convert list of dict to list of Tweet objects
tweets = [Tweet(tweet) for tweet in data]
print("\nSample tweet data")
print(tweets[0])

# Get data on languages used in tweets
languages = Counter([t.language for t in tweets])
print(f"Total languages used: {len(languages.keys())}")

# Plot most frequently used languages
languages_to_plot = 6
most_common_languages = languages.most_common(languages_to_plot)
language, count = zip(*most_common_languages)
figure, axes = plt.subplots()
axes.bar(language, count)
plt.title("Languages Used in Tweets")
plt.xlabel("Language")
plt.ylabel("Number of Tweets")
for i, v in enumerate(count):  # Used to plot values; centering imperfect
    plt.text(i - 0.25, v + (max(count) * 0.01), str(v))
plt.show()

# Get the English tweets
english_tweets = list(filter(lambda x: x.language == "English", tweets))
print(len(english_tweets))
