import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 600

masseage = "Pollinate... or else"
bee = Actor('bee.png')
bee.pos = 100,100
flower = Actor('flower.png')
flower.pos = 200, 200


def draw():
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()

def update():
    if keyboard.left:
        bee.x = bee.x - 2
    elif keyboard.right:
        bee.x = bee.x + 2
    elif keyboard.up:
        bee.y = bee.y - 2
    elif keyboard.down:
        bee.y = bee.y + 2


pgzrun.go()
