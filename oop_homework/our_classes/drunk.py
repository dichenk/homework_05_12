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

class DataBase:
    __counter = None
    def __new__(cls, *args, **kwargs):
        if DataBase.__counter == None:
            DataBase.__counter = super().__new__(cls)
        return DataBase.__counter
        
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connection with database: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('close connection with database')

    def read(self):
        return 'data from database'

    def write(self, data):
        print(f'writing to database {data}')



