class Bottle:

    def __init__(self, colour, value):
        self.colour = colour
        self.value = value

class Bottle_fill:

    def __init__(self, colour, contains = 0):
        self.colour = colour
        self.contains = contains

    def get_content(self):
        return self.contains

    def fill(self, volume):
        self.contains += volume

