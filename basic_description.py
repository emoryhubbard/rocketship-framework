from object_found import object_found
from point import Point
from color import Color
import constants
from drawable import Drawable

class BasicDescription(Drawable):

    def __init__(self):

        super().__init__()
        self._text = "Basic description"
        self._font_size = 30
        self._color = Color(245,245,245)
        self._position = Point(0, 0)
        self._velocity = Point(0,0)
        self._lines = []
        self._lines.append("Finding items in the debris...")
