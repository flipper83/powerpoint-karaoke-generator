from powerpointkaraoke.image_provider import ImageProvider
from powerpointkaraoke.karaoke_presentation import KaraokePresentation


class KaraokeGenerator:
    image_provider = None

    def __init__(self, image_provider):
        self.image_provider = image_provider

    def init_power_point(self, title, subtitle):
        karaoke_presentation = KaraokePresentation()
        karaoke_presentation.init(title, subtitle)
        return karaoke_presentation

    def add_slides(self, powerpoint_karaoke, num_slides):
        for index_slide in range(0, num_slides):
            image_downloaded = self.image_provider.next_image()
            powerpoint_karaoke.add_image_slide(image_downloaded)

    def generate(self):
        num_slides = 10
        powerpoint_karaoke = self.init_power_point("title", "subtitle")
        self.add_slides(powerpoint_karaoke, num_slides)
        powerpoint_karaoke.save()


if __name__ == '__main__':
    image_provider = ImageProvider()
    karaoke_generator = KaraokeGenerator(image_provider)
    karaoke_generator.generate()
