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

class TodoList:
    
    def __init__(self, task = "empty"):
        self.tasks = [task]

    def add_task(self, task):
        if self.tasks == ['empty']:
            self.tasks = [task]
        else:
            self.tasks.append(task)




