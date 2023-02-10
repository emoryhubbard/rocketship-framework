class Color:

    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = 255

    def get_red(self):
        return self._red
    
    def get_green(self):
        return self._green

    def get_alpha(self):
        return self._alpha

    def get_blue(self):
        return self._blue

    def set_red(self, red):
        self._red = red

    def set_green(self, green):
        self._green = green

    def set_blue(self, blue):
        self._blue = blue

    def set_alpha(self, alpha):
        self._alpha = alpha
    

    def to_tuple(self):
        return (self._red, self._green, self._blue, self._alpha)