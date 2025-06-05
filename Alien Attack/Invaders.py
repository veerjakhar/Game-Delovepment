import pgzrun
from random import randint

HEIGHT = 400
WIDTH = 400
message = "Attack on alien"
TITLE = "Alien Attack"
alien = Actor('alien.png')


def draw():
    screen.clear()
    screen.fill( color = (128, 0, 0))
    alien.draw()
    screen.draw.text(message, center = (200, 10), fontsize = 30)

def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot!"
        place_alien()
    else:
        message = "You FALIED!!!!!!!"


place_alien()
pgzrun.go()