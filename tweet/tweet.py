#!/usr/bin/env python3
#
#   A. Gnias
#
#   Linux 5.3.0-40-generic #32-Ubuntu
#   Python 3.7.5
#   Vim 8.1


class Tweet:
    def __init__(self, csv_dict):
        self.external_author_id = csv_dict.get("external_author_id")
        self.author = csv_dict.get("author")
        self.content = csv_dict.get("content")
        self.region = csv_dict.get("region")
        self.language = csv_dict.get("language")
        self.publish_date = csv_dict.get("publish_date")
        self.harvested_date = csv_dict.get("harvested_date")
        self.following = csv_dict.get("following")
        self.followers = csv_dict.get("followers")
        self.updates = csv_dict.get("updates")
        self.post_type = csv_dict.get("post_type")
        self.account_type = csv_dict.get("account_type")
        self.retweet = csv_dict.get("retweet")
        self.account_category = csv_dict.get("account_category")
        self.new_june_2018 = csv_dict.get("new_june_2018")
        self.alt_external_id = csv_dict.get("alt_external_id")
        self.tweet_id = csv_dict.get("tweet_id")
        self.article_url = csv_dict.get("article_url")
        self.tco1_step1 = csv_dict.get("tco1_step1")
        self.tco2_step1 = csv_dict.get("tco2_step1")
        self.tco3_step1 = csv_dict.get("tco3_step1")

    def __str__(self):
        return_string = str()
        return_string += "External Author ID: " + self.external_author_id + "\n"
        return_string += "Author: " + self.author + "\n"
        return_string += "Content: " + self.content + "\n"
        return_string += "Region: " + self.region + "\n"
        return_string += "Language: " + self.language + "\n"
        return_string += "Publish Date: " + self.publish_date + "\n"
        return_string += "Harvested Date: " + self.harvested_date + "\n"
        return_string += "Following: " + self.following + "\n"
        return_string += "Followers: " + self.followers + "\n"
        return_string += "Updates: " + self.updates + "\n"
        return_string += "Post Type: " + self.post_type + "\n"
        return_string += "Account Type: " + self.account_type + "\n"
        return_string += "Retweet: " + self.retweet + "\n"
        return_string += "Account Category: " + self.account_category + "\n"
        return_string += "New June 2018: " + self.new_june_2018 + "\n"
        return_string += "Alternative External ID: " + self.alt_external_id + "\n"
        return_string += "Tweet ID: " + self.tweet_id + "\n"
        return_string += "Article URL: " + self.article_url + "\n"
        return_string += "TCO1 Step 1:" + self.tco1_step1 + "\n"
        return_string += "TCO2 Step 1:" + self.tco2_step1 + "\n"
        return_string += "TCO3 Step 1:" + self.tco3_step1 + "\n"
        return return_string
