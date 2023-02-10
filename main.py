from cast import Cast
from player import Player
from script import Script
from move_actors_action import MoveActorsAction
from draw_actors_action import DrawActorsAction
from control_actors_action import ControlActorsAction
from director import Director
from output_service import OutputService
from input_service import InputService
from basic_item import basic_item
from point import Point
from load_assets_action import LoadAssetsAction
from unload_assets_action import UnloadAssetsAction
from basic_description import BasicDescription
from handle_collisions_action import HandleCollisionsAction
import constants
import random
from portrait import Portrait

def main():

    cast = Cast()
    player = Player()
    cast.add_actor("players", player)
    cast.add_actor("basic_description", BasicDescription())
    cast.add_actor("portrait", Portrait())
    #add more actors here
    print("added player")

    output_service = OutputService(player)
    #outputservice needs to be started with a player in order to calculate changes due to screen motion
    input_service = InputService()

    
    addRandomBasicItems(cast, output_service)

    script = Script()
    script.add_action("loading", LoadAssetsAction(output_service))
    script.add_action("unloading", UnloadAssetsAction(output_service))
    script.add_action("input", ControlActorsAction(input_service))
    script.add_action("update", MoveActorsAction(output_service))
    script.add_action("update", HandleCollisionsAction())
    #move actors needs output service too because actors need to get deltatime to update their positions
    #which is in output service
    script.add_action("output", DrawActorsAction(output_service))
    #add more scripts here, like collisions

    director = Director(output_service)
    director.start_game(cast, script)

def addBasicItemsForTesting(cast, output_service):
    positions = [[45, 45],
        [800, 800],
        [20, 800],
        [1500, 1500]]
    for position in positions:
        testItem = basic_item(Point(position[0], position[1]), output_service)
        cast.add_actor("basic_items", testItem)

def addRandomBasicItems(cast, output_service):
    column_start_y = 0 - constants.MAX_Y * 5
    sectors = []
    for i in range(0, 10):
        y_position = column_start_y + i * constants.MAX_Y
        addSectorRow(y_position, sectors)

    for sector in sectors:
        for position in sector:
            testItem = basic_item(Point(position._x, position._y), output_service)
            cast.add_actor("basic_items", testItem)

def testSector(cast, output_service):
    sec1 = createSector(0, 0)
    for position in sec1:
        testItem = basic_item(Point(position._x, position._y), output_service)
        cast.add_actor("basic_items", testItem)

def addSectorRow(y, sectors):
    row_start_x = 0 - constants.MAX_X * 5
    for i in range(0, 10):
        x_position = row_start_x + i * constants.MAX_X
        sector = createSector(x_position, y)
        sectors.append(sector)

def createSector(x, y):
    sector = []
    totalCount = random.randint(2, 4)
    for i in range(0, totalCount):
        randx = x + random.randint(0, constants.MAX_X)
        randy = y + random.randint(0, constants.MAX_Y)

        sector.append(Point(randx, randy))
    
    return sector

if __name__ == "__main__":
    main()