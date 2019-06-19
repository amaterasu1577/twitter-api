# app/apis/tweets.py
from flask_restplus import Namespace, Resource, fields
from app.db import tweet_repository


api = Namespace('tweets')

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet
