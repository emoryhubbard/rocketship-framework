import constants
from action import Action
from point import Point
from input_service import InputService

class ControlActorsAction(Action):

    def __init__(self, input_service):
        self._input_service = input_service

    def execute(self, cast):
        x = 0
        y = 0

        if self._input_service.is_key_down("a"):
            x = -1

        if self._input_service.is_key_down("d"):
            x = 1
        
        if self._input_service.is_key_down("w"):
            y = -1
        
        if self._input_service.is_key_down("s"):
            y = 1

        direction = Point(x, y)
        player = cast.get_first_actor("players")
        player.set_direction(direction)