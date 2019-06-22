import random

from powerpointkaraoke.chart_text_provider import TextChartProvider
from powerpointkaraoke.image_provider import ImageProvider
from powerpointkaraoke.imagesources.reddit_image_source import RedditImageSource
from powerpointkaraoke.karaoke_presentation import KaraokePresentation

SLIDE_IMAGE = 0
SLIDE_PIE_GRAPH = 1
SLIDE_BAR_GRAPH = 2


class KaraokeGenerator:
    image_provider = None
    chart_text_provider = None
    karaoke_presentation = KaraokePresentation()

    def __init__(self, image_provider, text_chart_provider):
        self.image_provider = image_provider
        self.chart_text_provider = text_chart_provider

    def init_power_point(self, title, subtitle):
        self.karaoke_presentation.init(title, subtitle)
        return self.karaoke_presentation

    def add_slides(self, num_slides):
        for index_slide in range(0, num_slides):
            type_slide_to_add = self.obtain_type_of_slide()
            self.add_slide_by_type(type_slide_to_add)

    def add_slide_by_type(self, kind_slide_to_add):
        if kind_slide_to_add == SLIDE_IMAGE:
            image_downloaded = self.image_provider.next_image()
            self.karaoke_presentation.add_image_slide(image_downloaded)
        elif kind_slide_to_add == SLIDE_PIE_GRAPH:
            self.karaoke_presentation.add_pie_chart(self.chart_text_provider.next_titles())
        else:
            self.karaoke_presentation.add_bar_chat(self.chart_text_provider.next_titles())

    def generate(self):
        num_slides = 10
        title = "Hello"
        subtitle = "World"
        self.karaoke_presentation.init(title, subtitle)
        self.add_slides(num_slides)
        self.karaoke_presentation.save()

    @staticmethod
    def obtain_type_of_slide():
        percentage = random.randint(0, 100)
        if percentage < 90:
            return SLIDE_IMAGE
        elif percentage < 95:
            return SLIDE_PIE_GRAPH
        else:
            return SLIDE_BAR_GRAPH


if __name__ == '__main__':
    image_provider = ImageProvider([RedditImageSource()])
    text_chart_provider = TextChartProvider()
    karaoke_generator = KaraokeGenerator(image_provider=image_provider, text_chart_provider=text_chart_provider)
    karaoke_generator.generate()
