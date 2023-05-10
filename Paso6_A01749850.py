
from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)
   
 #Important to do the circle code(the complicated way)
"""        
import math

def circle(start, end):
    "Draw circle from start to end."
    radius = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    center_x = start.x + (end.x - start.x) / 2
    center_y = start.y + (end.y - start.y) / 2
    center = vector(center_x, center_y)

    up()
    goto(center.x, center.y - radius)
    down()
    circle = 2 * math.pi * radius

    for _ in range(360):
        forward(circle / 360)
        left(1)
"""

def draw_circle(start, end):  #Aqui para realizar un ciorculo se utilizo la operacion del radio para que pudiera tener un punto de partidas y realmente dibujara algo y no solo girara
    """Draw circle from start to end."""
    radio = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
    up()
    goto(start.x, start.y - radio)
    down()
    begin_fill()
    circle(radio)
    end_fill()
        
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    
    forward(end.x-start.x)
    left(90)
    forward(end.y-end.x)
    left(90)
    forward(end.x-start.x)
    left(90)
    forward(end.y-end.x)
    left(90)
    
    end_fill()
    

def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    
    for _ in range(3):
        forward(end.x-start.x)
        left(120)
#120 due to the adition of the exterior angles which has to be 360. The rotation is of three consecutive left turns of 120 degrees each
        end_fill()
        
        
#parte del código      
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None
        
        
def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()


