from object_found import object_found
from point import Point
from color import Color
import constants

class LegendaryItem(object_found):

    def __init__(self, point, output_service):

        super().__init__()
        self._text = "L"
        self._font_size = 15
        self._color = Color(245,245,245)
        self._position = Point(point._x, point._y)
        self._velocity = Point(0,0)
        self._output_service = output_service
        self._name = ""
        self._file = ""
        self._lines = []

    def found_object(self):
        pass
