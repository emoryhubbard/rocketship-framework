from object_found import object_found
from point import Point
from color import Color
import constants
from drawable import Drawable

class Portrait(Drawable):

    def __init__(self):

        super().__init__()
        self._text = "Portrait object"
        self._font_size = 15
        self._color = Color(245,245,245)
        self._position = Point(0, 0)
        self._velocity = Point(0,0)
        self._file = None