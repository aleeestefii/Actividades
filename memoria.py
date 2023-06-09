from random import *
from turtle import *

from freegames import path

car = path('car.gif')
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F',
           'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F'] #en vez de usar numeros, use letras. Igualmente, para que la matriz fuera de 64, repetí letras. 
state = {'mark': None}
hide = [True] * 64
tiles_hidden = 64
taps = 0 # Se crea una variable que permita
         # contar el numero de taps (clicks)
mensaje = "¡Felicidades, has ganado el juego!"

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps # se usa la variable de global para llamar taps
    global tiles_hidden
    taps += 1
    print("Taps: ", taps)
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or letters[mark] != letters[spot]:#como la variable de 'tiles' cambió a letters, igual las funciones o parte dle código que contenía info. de 'tiles'
        state['mark'] = spot
        
        
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        tiles_hidden -= 2

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(letters[mark], font=('Arial', 30, 'normal'))

    if tiles_hidden == 0:
        textinput("Ganaste!", mensaje)
        exit()

    update()
    ontimer(draw, 100)


shuffle(letters)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
