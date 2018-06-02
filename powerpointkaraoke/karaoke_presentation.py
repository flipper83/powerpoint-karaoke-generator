from pptx import Presentation
from pptx.util import Inches, Pt, Emu

SLD_LAYOUT_TITLE = 0
SLD_LAYOUT_IMAGE = 6


class KaraokePresentation:
    presentation = None

    def init(self, title_value, subtitle_value):
        self.presentation = Presentation()
        title_slide_layout = self.presentation.slide_layouts[SLD_LAYOUT_TITLE]
        slide = self.presentation.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]
        title.text = title_value
        subtitle.text = subtitle_value

    def add_image_slide(self):
        image_layout = self.presentation.slide_layouts[SLD_LAYOUT_IMAGE]
        slide = self.presentation.slides.add_slide(image_layout)

        top = Inches(0)
        left = Inches(0)
        height = Inches(7.5)
        picture = slide.shapes.add_picture("image.jpg", left, top, height=height)

        pos_x = (self.presentation.slide_width.inches - Emu(picture.width).inches) / 2
        picture.left = Inches(pos_x).emu

    def save(self):
        self.presentation.save('test.pptx')
