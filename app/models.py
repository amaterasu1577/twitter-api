# app/app_models.py
"""
Implement a Tweet class
"""
from datetime import datetime


class Tweet():
    def __init__(self, text):
        self.text = text
        self.created_at = datetime.now().strftime("%d/%m/%Y-%I:%M")
        self.id = None

class TweetRepository():
    def __init__(self, tweet):
        self.tweet_list = {0: tweet.text}
