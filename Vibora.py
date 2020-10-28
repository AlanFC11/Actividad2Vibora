from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colores = ['black', 'green', 'blue', 'yellow', 'orange']
colorVibora = colores[0]
colorComida = colores[0]
while colorVibora == colorComida:
    colorVibora = colores[randrange(0,4)]
    colorComida = colores[randrange(0,4)]

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorVibora)

    square(food.x, food.y, 9, colorComida)
    update()
    ontimer(move, 100)

def moveFood():
    #direccion = randrange(-1,2)
    nuevaPosicion = 17
    while nuevaPosicion > 15 or nuevaPosicion < -15:
        direccion = randrange(-1,2)
        if direccion == -1:
            food.x = (food.x - 1)*10
            nuevaPosicion = food.x-1
        elif direccion == 2:
            food.x = (food.x + 1)*10
            nuevaPosicion = food.x+1
        elif direccion == 0:
            food.y = (food.y - 1)*10
            nuevaPosicion = food.y-1
        elif direccion == 1:
            food.y = (food.y + 1)*10
            nuevaPosicion = food.y+1
            
    update()
    ontimer(moveFood,100)
        
        
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()