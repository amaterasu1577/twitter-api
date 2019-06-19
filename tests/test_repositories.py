# tests/test_repositories.py
from unittest import TestCase
from app.models import Tweet  # We will code our `TweetRepository` class in `app/models.py`
from app.repositories import TweetRepository


class TestRepository(TestCase):
    def test_instance_variables(self):
        # Create an instance of the `Repository` class with one tweet
        # we initialize first
        tweet = Tweet('Test tweet')
        repository = TweetRepository(tweet)
        # Check that the repository as a tweet_list parameter
        self.assertIsNotNone(repository.tweet_list)
        # Check that `repository` holds a dictionary
        self.assertIsInstance(repository.tweet_list, dict)
        """ Check that when creating a new `repository` instance,
        we could retrieve the tweet message """
        self.assertEqual(repository.tweet_list[0], 'Test tweet')

    def test_add_tweet(self):
        repository = TweetRepository()
        tweet = Tweet("a new tweet")
        repository.add(tweet)
        self.assertEqual(len(repository.tweets), 1)

    def test_auto_increment_of_ids(self):
        repository = TweetRepository()
        first_tweet = Tweet("a first tweet")
        repository.add(first_tweet)
        self.assertEqual(first_tweet.id, 1)
        second_tweet = Tweet("a second tweet")
        repository.add(second_tweet)
        self.assertEqual(second_tweet.id, 2)

    def test_get_tweet(self):
        repository = TweetRepository()
        tweet = Tweet("a new tweet")
        repository.add(tweet)
        self.assertEqual(tweet, repository.get(1))
        self.assertIsNone(repository.get(2))
