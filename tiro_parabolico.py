"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score = 0#se añadió la variable score

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.35

    if inside(ball):
        speed.y -= 0.15 # se modifica hacia abajo la velocidad pues se realiza un tiro parabolico
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
                global score
                score+=1 # Se incrementa el score para cuando el objetivo sea golpeado, para que en vez de que se pare
                # cuando los objetivos lleguen al fin, este no se acabe. 

    draw()

    for target in targets:
        if not inside(target):
            target.x=200
            target.y=randrange(-150,150)#Añadí un objetivo no válido, con una nueva coordenada -y

    ontimer(move, 50) # de igual manera se modifica el numero para abajo por 
                     # la direccion en la que se mueve #Lo cambie por 50
#Se añadió una función de show_score                    
def show_score():
    """ To Display the current score."""
    goto(-190, 180)
    color('black')
    write(f"Score: {score}", align='left')

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
show_score()
done()
