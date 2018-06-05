import random
import urllib.request

import praw


class RedditImageSource(object):
    reddit = None
    filename = "reddit_image.jpg"

    def __init__(self):
        self.reddit = praw.Reddit(client_id='YKo_9gh5XpDJYQ',
                                  client_secret=None,
                                  redirect_uri='http://localhost:8080',
                                  user_agent='karaoke')
        self.reddit.read_only = True

    def next_image(self):
        submission = self.reddit.subreddit('Funnypics').random()
        url = submission.preview['images'][0]['source']['url']
        urllib.request.urlretrieve(url, self.filename)
        return self.filename
