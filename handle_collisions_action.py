from action import Action
from point import Point
import constants

class HandleCollisionsAction(Action):
    def __init__(self):
        pass

    def execute(self, cast):
        player = cast.get_first_actor("players")
        p = player.get_position()

        basic_items = cast.get_actors("basic_items")
        basic_description = cast.get_first_actor("basic_description")
        for basic_item in basic_items:
            p2 = basic_item.get_position()
            if self.is_point_close(p, p2):
                print("isClose")
                desc = basic_item._description
                basic_description._lines = [desc]

        legendary_items = cast.get_actors("legendary_items")
        legendary_description = cast.get_first_actor("basic_description")
        portrait = cast.get_first_actor("portrait")
        closeToLegendary = False
        for legendary_item in legendary_items:
            p2 = legendary_item.get_position()
            if self.is_point_close(p, p2):
                print("isClose")
                closeToLegendary = True
                lines = legendary_item._lines
                legendary_description._lines = lines.copy()
                legendary_description.set_position(Point(constants.MAX_X / 2, 0))
                portrait._file = legendary_item._file
                portrait._name = legendary_item._name
                portrait._lines = legendary_item._lines
        if closeToLegendary == False:
            portrait._file = None
            legendary_description.set_position(Point(0, 0))
            if len(legendary_description._lines) > 1:
                legendary_description._lines = ["Finding items in the debris..."]

    def is_close(self, x, otherx):
        is_close = False
        precision = 25
        lower_limit = otherx - precision
        upper_limit = otherx + precision

        if lower_limit <= x <= upper_limit:
            is_close = True

        return is_close

    def is_point_close(self, p, otherp):
        if self.is_close(p._x, otherp._x) and self.is_close(p._y, otherp._y):
            return True
        else:
            return False
