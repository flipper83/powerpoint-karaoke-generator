from powerpointkaraoke.karaoke_presentation import KaraokePresentation


def init_power_point(title, subtitle):
    karaoke_presentation = KaraokePresentation()
    karaoke_presentation.init(title, subtitle)
    return karaoke_presentation


if __name__ == '__main__':
    powerpointKaraoke = init_power_point("title", "subtitle")
    powerpointKaraoke.add_image_slide()
    powerpointKaraoke.save()
