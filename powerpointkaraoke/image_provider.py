import random
import urllib.request

import praw


class ImageProvider(object):
    reddit = None

    def __init__(self):
        self.reddit = praw.Reddit(client_id='YKo_9gh5XpDJYQ',
                     client_secret= None,
                     redirect_uri='http://localhost:8080',
                     user_agent='karaoke')
        self.reddit.read_only = True

    def next_image(self):
        images = []
        for submission in self.reddit.subreddit('Funnypics').new():
            images.append(submission.preview['images'][0]['source']['url'])

        image_to_download = random.choice(images)
        urllib.request.urlretrieve(image_to_download, "image.jpg")
        return "image.jpg"
