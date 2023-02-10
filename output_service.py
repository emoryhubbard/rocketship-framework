HEIGHT = 900
WIDTH = 1500
import pyray
import constants
from datetime import datetime
import pathlib
import constants
from player import Player
from color import Color
import random

class OutputService():
    def __init__(self, player):
        pass
        self._cur_time = datetime.now()
        self._player = player
        self._textures = {}
        self._basic_descriptions = []

    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
    
    def draw_actor(self, actor):
        if actor.has_actors() == True:
            for member in actor.get_actors():
                self.draw_single_actor(member)
        else:
            self.draw_single_actor(actor)

    def draw_basic_item(self, actor):
        text = actor.get_text()
        x = actor.get_position().get_x() - (self._player.get_position().get_x() - constants.MAX_X / 2)
        y = actor.get_position().get_y() - (self._player.get_position().get_y() - constants.MAX_Y / 2)
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, int(x), int(y), font_size, color)

    def draw_legendary_item(self, actor):
        text = actor.get_text()
        x = actor.get_position().get_x() - (self._player.get_position().get_x() - constants.MAX_X / 2)
        y = actor.get_position().get_y() - (self._player.get_position().get_y() - constants.MAX_Y / 2)
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, int(x), int(y), font_size, color)


    def draw_basic_description(self, actor):
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        for line in actor._lines:
            pyray.draw_text(line, int(x), int(y), font_size, color)
            y = y + 30

    def draw_portrait(self, actor):
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()

        position = pyray.Vector2(x, y)
        scale = 1
        rotation = 0
        tint = pyray.Color(255, 255, 255, 255)
        if actor._file != None:
            print(actor._file)
            print(actor._name)
            print(actor._lines)
            texture = self._textures[actor._file]
            pyray.draw_texture_ex(texture, position, rotation, scale, tint)

    def draw_single_actor(self, actor):
        text = actor.get_text()
        x = actor.get_position().get_x() - (self._player.get_position().get_x() - constants.MAX_X / 2)
        y = actor.get_position().get_y() - (self._player.get_position().get_y() - constants.MAX_Y / 2)
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, int(x), int(y), font_size, color)

    def draw_player(self, actor):
        center_x = constants.MAX_X / 2
        center_y = constants.MAX_Y / 2
        x = center_x - 56/2
        y = center_y - 56/2
        color = actor.get_color().to_tuple()
        direction = actor.get_direction()
        if direction._x == 0 and direction._y == 0:
            direction = actor._prev_direction

        if direction._x == 0 and direction._y == -1:
            texture = self._textures["images/RocketUp.png"]
        elif direction._x == 1 and direction._y == -1:
            texture = self._textures["images/RocketUpRight.png"]
        elif direction._x == 1 and direction._y ==0:
            texture = self._textures["images/RocketRight.png"]
        elif direction._x == 1 and direction._y == 1:
            texture = self._textures["images/RocketDownRight.png"]
        elif direction._x == 0 and direction._y ==1:
            texture = self._textures["images/RocketDown.png"]
        elif direction._x == -1 and direction._y == 1:
            texture = self._textures["images/RocketDownLeft.png"]
        elif direction._x == -1 and direction._y == 0:
            texture = self._textures["images/RocketLeft.png"]
        elif direction._x == -1 and direction._y == -1:
            texture = self._textures["images/RocketUpLeft.png"]
        else:
            texture = self._textures["images/RocketUp.png"]

        position = pyray.Vector2(x, y)
        scale = 1
        rotation = 0
        tint = pyray.Color(255, 255, 255, 255)
        pyray.draw_texture_ex(texture, position, rotation, scale, tint)
    def draw_display(self, actor):
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        pyray.draw_text(text, int(x), int(y), font_size, color)

    def flush_buffer(self):
        pyray.end_drawing()

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.TITLE)
        pyray.set_target_fps(constants.FRAME_RATE)

    def do_updates(self):
        self._prev_time = self._cur_time
        self._cur_time = datetime.now()

    def get_delta_time(self): #returns change in time since last update in seconds
        delta_time = self._cur_time - self._prev_time #DOES NOT return float, returns timedelta object due to datetime API
        return delta_time.total_seconds() #DOES return float

    def load_image(self, file):
        texture = pyray.load_texture(file)
        self._textures[file] = texture

    def unload_image(self, file):
        texture = self._textures[file]
        pyray.unload_texture(texture)

    def test_draw():
        output_service = OutputService(Player())
        output_service.open_window()

        filepath = "RocketUp.png"
        #filepath = str(pathlib.Path(filepath))
        texture = pyray.load_texture(filepath)
        x = constants.MAX_X / 2
        y = constants.MAX_Y / 2
        position = pyray.Vector2(x, y)
        scale = 1
        rotation = 0
        tint = pyray.Color(255, 255, 255, 255)

        while (output_service.is_window_open()):
            output_service.do_updates()
           # test_object.do_updates()
            output_service.clear_buffer()
            pyray.draw_texture_ex(texture, position, rotation, scale, tint)
            output_service.flush_buffer()

        pyray.unload_texture(texture)
        output_service.close_window()
    
    def test_function():
        output_service = OutputService(Player())
        output_service.open_window()
        #input_service = InputService()

        #test_object = DrawablePlayer(output_service, input_service)
        #test_object.set_position(Point(0, 0))

        while (output_service.is_window_open()):
            output_service.do_updates()
           # test_object.do_updates()
            output_service.clear_buffer()
            #test_object.draw()
            output_service.flush_buffer()

        output_service.close_window()

    def get_basic_description(self):
        length = len(self._basic_descriptions)
        randomIndex = random.randint(0, length-1)
        return self._basic_descriptions[randomIndex]

def main():
    OutputService.test_draw()

if __name__ == "__main__":
    main()
