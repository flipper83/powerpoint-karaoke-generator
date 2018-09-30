import random

from PIL import Image
from pptx import Presentation
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches, Emu

SLD_LAYOUT_TITLE = 0
SLD_LAYOUT_IMAGE = 6
SLD_LAYOUT_CHART = 6


def random_values(size):
    values = []
    for index_slide in range(0, size):
        values.append(random.randint(5, 100))
    return values


class KaraokePresentation:
    presentation = None

    def __init__(self):
        self.presentation = Presentation()

    def init(self, title_value, subtitle_value):
        title_slide_layout = self.presentation.slide_layouts[SLD_LAYOUT_TITLE]
        slide = self.presentation.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]
        title.text = title_value
        subtitle.text = subtitle_value

    def add_bar_chat(self, categories):
        chart_layout = self.presentation.slide_layouts[SLD_LAYOUT_CHART]
        slide = self.presentation.slides.add_slide(chart_layout)

        chart_data = ChartData()
        chart_data.categories = categories
        values = random_values(len(categories))
        chart_data.add_series('Serie', values)

        # add chart to slide --------------------
        x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
        slide.shapes.add_chart(
            XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data)

    def add_image_slide(self, image_downloaded):
        image_layout = self.presentation.slide_layouts[SLD_LAYOUT_IMAGE]
        slide = self.presentation.slides.add_slide(image_layout)

        picture = self.picture_fitted(slide, image_downloaded)

        pos_x = (self.presentation.slide_width.inches - Emu(picture.width).inches) / 2
        picture.left = Inches(pos_x).emu

    def save(self):
        self.presentation.save('test.pptx')

    def get_image_size(self, image_downloaded):
        im = Image.open(image_downloaded)
        return im.size

    def picture_fitted(self, slide, image_downloaded):
        top = Inches(0)
        left = Inches(0)
        height = Inches(7.5)
        width = Inches(10)
        source_width, source_height = self.get_image_size(image_downloaded)
        if source_width > source_height:
            return slide.shapes.add_picture(image_downloaded, left, top, height=height)
        else:
            return slide.shapes.add_picture(image_downloaded, left, top, width=width)
