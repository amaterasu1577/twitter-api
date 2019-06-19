# tests/test_repositories.py
from unittest import TestCase
from app.models import Tweet, TweetRepository  # We will code our `TweetRepository` class in `app/models.py`


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
