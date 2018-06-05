import random


class ImageProvider(object):
    image_sources = []

    def __init__(self, image_sources):
        self.image_sources = image_sources

    def next_image(self):
        image_source = random.choice(self.image_sources)
        return image_source.next_image()
