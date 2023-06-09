"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
import random #se importa random para poder elegir un color al azar
from turtle import *

from freegames import square, vector

colores = ['orange', 'yellow', 'green', 'blue', 'purple'] # se crea la variante de colores para agregar colores distintos
snake_color = random.choice(colores) # se crean dos variables, una para la serpiente
food_color = random.choice(colores) # otra para la comida
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y): 
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
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
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)
    
#función para que la comida pueda moverse
def movefood():
    food.x= randrange(-15,15)*10
    food.y= randrange(-15,15)*10
    ontimer(movefood,4000) #4secs



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movefood()#se añade aquí, para que se ejecute la función
done()
