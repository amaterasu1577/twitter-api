# app/app_repositories.py
"""
Implement a TweetRepository class
"""


class TweetRepository():
    def __init__(self, tweet):
        self.tweet_list = {0: tweet.text}
