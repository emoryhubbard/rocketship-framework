from action import Action
import os
from legendary_item import LegendaryItem
from point import Point
import constants
import random

class LoadAssetsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        basic_file = open("basic_items.txt", "r")
        basic_descriptions = basic_file.readlines()
        basic_file.close()
        self._output_service._basic_descriptions = basic_descriptions
        basic_items = cast.get_actors("basic_items")
        for basic_item in basic_items:
            basic_item.load_description()

        for file in os.listdir("images"):
            self._output_service.load_image("images/" + file)
        
        self.load_legendary_items(cast)

    def load_legendary_items(self, cast):
        endOfFile = False
        file = open("legendary_items.txt", "r")
        
        while not endOfFile:
            line = file.readline()
            if line == "":
                endOfFile = True
            
            if endOfFile != True:
                legendary_item = LegendaryItem(Point(0, 0), cast)
                legendary_item._name = line.strip()
                #legendary_item._lines.append(line)
                legendary_item._file = ("images/" + file.readline()).strip()
                
                newLine = False
                while not newLine:
                    line = file.readline()
                    if line == "\n" or line == "":
                        newLine = True
                    else:
                        legendary_item._lines.append(line)
                cast.add_actor("legendary_items", legendary_item)         
        file.close()
        #self.testSector(cast, self._output_service)
        self.randomly_place_legendaries(cast)
        
    def testSector(self, cast, output_service):
        sec1 = self.createSector(0, 0)
        legendary_items = cast.get_actors("legendary_items")
        legendary_index = 0

        for position in sec1:
            if not legendary_index > len(legendary_items) - 1:
                legendary_items[legendary_index].set_position(Point(position._x, position._y))
                legendary_index = legendary_index + 1
    def randomly_place_legendaries(self, cast):
        legendary_items = cast.get_actors("legendary_items")
        rand_points = [Point(random.randint(0, constants.MAX_X), random.randint(0, constants.MAX_Y))]
        print(legendary_items)
        for i in range(0, len(legendary_items)):
            rand_points.append(Point(random.randint(- 5 * constants.MAX_X, 5 * constants.MAX_X), random.randint(-5 * constants.MAX_Y, 5 * constants.MAX_Y)))
        print(rand_points)
        random.shuffle(rand_points)
        i = 0
        for legendary in legendary_items:
            legendary.set_position(rand_points[i])
            i = i + 1
    def randomize_legendary_positions(self, cast):
        column_start_y = 0 - constants.MAX_Y * 5
        sectors = []
        for i in range(0, 10):
            y_position = column_start_y + i * constants.MAX_Y
            self.addSectorRow(y_position, sectors)

        for sector in sectors:
            for position in sector:
                testItem = LegendaryItem(Point(position._x, position._y), self._output_service)
                cast.add_actor("legendary_items", testItem)
    def addSectorRow(self, y, sectors):
        row_start_x = 0 - constants.MAX_X * 5
        for i in range(0, 10):
            x_position = row_start_x + i * constants.MAX_X
            sector = self.createSector(x_position, y)
            sectors.append(sector)

    def createSector(self, x, y):
        sector = []
        totalCount = 1
        for i in range(0, totalCount):
            randx = x + random.randint(0, constants.MAX_X)
            randy = y + random.randint(0, constants.MAX_Y)

            sector.append(Point(randx, randy))
        
        return sector

def main():
    for file in os.listdir("images"):
        print(file)

if __name__ == "__main__":
    main()
