from object_found import object_found
from point import Point
from color import Color
import constants

class basic_item(object_found):

    def __init__(self, point, output_service):

        super().__init__()
        self._text = "$"
        self._font_size = 15
        self._color = Color(245,245,245)
        self._position = Point(point._x, point._y)
        self._velocity = Point(0,0)
        self._output_service = output_service

    def found_object(self):
        pass

    def load_description(self):
        self._description = self._output_service.get_basic_description()
    