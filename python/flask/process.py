__author__ = 'grumps'
from PIL import Image

from settings import fg_image


def process(backgroundimage):
    """
    :param backgroundimage:
    :return backgroundimage + 33% of settings.fb_image:
    """
    bg = Image.open(backgroundimage)
    fg = Image.open(fg_image)

    def scale_fg(bg):
        """
        scales foreground to 33% of backgrounds shortest side
        :return: PIL.Image.thumbnail
        :note: foreground image as a modified object
        """

        resize = ()
        if (float(bg.size[1]) * .33 >= fg.size[1]) or (float(bg.size[0]) * .33 >= float(fg.size[0])):
            print "We're upscaling..."
        # downscale image to 33% of shortest side

        elif bg.size[0] > bg.size[1]:
            resize = (fg.size[0], int(0.33 * bg.size[1]))
        elif bg.size[0] <= bg.size[1]:
            resize = (int(0.33 * bg.size[0]), fg.size[1])
        if not resize:
            raise Exception
        else:
            return fg.thumbnail((resize))

    def get_center((x, y)):
        """
        get center of rectangle, given size
        :return: tuple (x,y)
        """
        return int(float(x) / 2), int(float(y) / 2)

    def get_upper_left(bg_center, fg_center):
        """
        get upper corner for fg image
        centered in bg
        :return: tuple(x,y)
        """
        upper_left_x = bg_center[0] - fg_center[0]
        upper_left_y = bg_center[1] - fg_center[1]
        return upper_left_x, upper_left_y

    def merge(upper_left):
        """
        :except bg, fb, upper_left:
        :return merged image:
        """
        return bg.paste(fg, (upper_left[0], upper_left[1]), fg)

    scale_fg(bg)
    position = get_upper_left(get_center(bg.size), get_center(fg.size))
    merge(position)
    return bg
