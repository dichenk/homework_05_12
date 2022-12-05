import our_classes.drunk as cheers

## какую домашку запускаем?
task = 4

if task == 1:
    
    bottle_1 = cheers.Bottle('red', 0.7)
    print(bottle_1.colour, bottle_1.value)

    bottle_2 = cheers.Bottle('white', 0.3)
    print(bottle_2.colour, bottle_2.value)

    bottle_3 = cheers.Bottle('black', 1.0)
    print(bottle_3.colour, bottle_3.value)

if task == 2:
    bottle_1 = cheers.Bottle_fill('red')
    bottle_2 = cheers.Bottle_fill('blue')

    print(bottle_1.colour, bottle_1.get_content())
    bottle_1.fill(100)
    print(bottle_1.colour, bottle_1.get_content())

    print(bottle_1.colour, bottle_2.get_content())
    bottle_2.fill(500)
    print(bottle_2.colour, bottle_2.get_content())

if task == 3:

    todo_list = cheers.TodoList()
    todo_list.add_task('to buy a bulb')
    todo_list.add_task('to change the bulb')
    todo_list.add_task('to throw out the bulb')
    print('\n'.join(todo_list.tasks))
    
if task == 4:
    db = cheers.DataBase('root', '1234', 80)
    print(db)
    db2 = cheers.DataBase('root2', '5678', 40)
    print(db2)
    print('db is db2, isnt it? ', db is db2)
