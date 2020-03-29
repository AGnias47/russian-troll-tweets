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
print(f"\nTotal languages used: {len(languages.keys())}")

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

# Followers reached
tweets.sort(key=lambda x: int(x.followers), reverse=True)
highest_followed = tweets[0]
print(f"\nMax followers reached: {highest_followed.followers}")
authors = list()
followers = list()
for t in tweets:
    if len(authors) == 5:
        break
    if t.author not in authors:
        authors.append(t.author)
        followers.append(int(t.followers))
figure, axes = plt.subplots()
axes.bar(authors, followers)
plt.title("Top Followed Accounts")
plt.xlabel("Accounts")
plt.ylabel("Number of Followers")
for i, v in enumerate(followers):  # Used to plot values; centering imperfect
    plt.text(i - 0.25, v + (max(followers) * 0.01), str(v))
plt.show()


# Get the English tweets
english_tweets = list(filter(lambda x: x.language == "English", tweets))
print(f"\nPerforming analysis on {len(english_tweets)} English tweets")

# English Followers reached
highest_followed_english = english_tweets[0]
print(f"\nMax English followers reached: {highest_followed_english.followers}")
english_authors = list()
english_followers = list()
for t in english_tweets:
    if len(english_authors) == 5:
        break
    if t.author not in english_authors:
        english_authors.append(t.author)
        english_followers.append(int(t.followers))
figure, axes = plt.subplots()
axes.bar(english_authors, english_followers)
plt.title("Top Followed Accounts")
plt.xlabel("Accounts")
plt.ylabel("Number of Followers")
for i, v in enumerate(english_followers):  # Used to plot values; centering imperfect
    plt.text(i - 0.25, v + (max(english_followers) * 0.01), str(v))
plt.show()

# Get individual words used in the tweets
tweet_content = [t.content for t in english_tweets]
words = list()
for tweet in tweet_content:
    for word in tweet.split(" "):
        words.append(word)
# Clean the data
words = utilities.data.clean_words_list(words)

# Plot the most frequently used words
words_nonhashtags = list(filter(lambda x: x[0] != "#", words))
word_count = Counter(words_nonhashtags)
most_common_words = word_count.most_common(10)
word, word_count_int = zip(*most_common_words)
word = [w.title() for w in word]
figure, axes = plt.subplots()
axes.bar(word, word_count_int)
plt.title("Most Frequenty Used Words in English Tweets")
plt.xlabel("Word")
plt.ylabel("Number of Occurrances")
for i, v in enumerate(word_count_int):  # Used to plot values; centering imperfect
    plt.text(i - 0.1, v + (max(word_count_int) * 0.01), str(v))
plt.show()

# Plot most frequently used hashtags
hashtags = list(filter(lambda x: x[0] == "#", words))
hashtag_count = Counter(hashtags)
most_common_hashtags = hashtag_count.most_common(10)
hashtag, hashtag_count = zip(*most_common_hashtags)
figure, axes = plt.subplots()
axes.bar(hashtag, hashtag_count)
plt.title("Most Frequenty Used Hashtags in English Tweets")
plt.xlabel("Word")
plt.ylabel("Number of Occurrances")
for i, v in enumerate(hashtag_count):  # Used to plot values; centering imperfect
    plt.text(i - 0.1, v + (max(hashtag_count) * 0.01), str(v))
plt.show()
