from drawable import Drawable
from color import Color
from point import Point
import constants

class Player(Drawable):

    def __init__(self):
        super().__init__()
        self._font_size = 15
        self._text = "O"
        self._color = Color(245,245,245)
        half_of_width = int(constants.MAX_X / 2)
        half_of_height = int(constants.MAX_Y / 2)
        self._position = Point(half_of_width, half_of_height)
        self._velocity = Point(0,0)
        self._speed = 400 #default speed is 200 pixels per second
        self._prev_direction = Point(0, -1)
        self._direction = Point(0, 0)

    def move_next(self, delta_time):
        self.update_velocity() #this updates velocity
        super().move_next(delta_time) #default method only updates position

    def set_direction(self, direction):
        if direction._x != 0 or direction._y != 0:
            self._prev_direction = direction
        self._direction = direction
        #print(f"set direction {direction._x} {direction._y}")
    def get_direction(self):
        return self._direction
    def update_velocity(self): #"update velocity" is a better name
        key_direction = self._direction
        new_x = key_direction._x * self._speed
        new_y = key_direction._y * self._speed
        self._velocity = Point(new_x, new_y)