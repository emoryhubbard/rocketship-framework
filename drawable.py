import constants
from color import Color
from point import Point

class Drawable:



    def __init__(self):

        self._text = ""
        self._font_size = 15
        self._color = Color(245,245,245)
        quarter_of_width = int(constants.MAX_X / 4)
        half_of_height = int(constants.MAX_Y / 2)
        self._position = Point(quarter_of_width, half_of_height)
        self._velocity = Point(0,0)

    def set_speed(self, speed):
        self._speed = speed
    
    def get_speed(self):
        return self._speed
    
    def get_color(self):

        return self._color

    def get_font_size(self):

        return self._font_size

    def get_position(self):

        return self._position

    def get_velocity(self):

        return self._velocity

    def move_next(self, delta_time):
        x = self._position._x + self._velocity._x * delta_time
        y = self._position._y + self._velocity._y * delta_time
        self._position = Point(x, y)
        
    def set_color(self,color):

        self._color = color

    def set_position(self, position):
        self._position = position

    def set_font_size(self,font_size):

        self._font_size = font_size

    def set_velocity(self, velocity):

        self._velocity = velocity

    def set_text(self, text):

        self._text = text

    def get_text(self):
        return self._text

    def has_actors(self):
        return False

    def get_actors(self):
        return None
