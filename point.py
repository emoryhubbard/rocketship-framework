class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def equals(self, point):
        is_equal = False
        if self._x == point._x and self._y == point._y:
            is_equal = True
        return is_equal

        

