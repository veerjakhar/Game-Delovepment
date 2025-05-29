import pgzrun

from random import randint

WIDTH = 300
HEIGHT = 300

def draw():  
    width = WIDTH
    height = HEIGHT - 200
    r = 255
    g = 0
    b = randint(120, 255)
    for i in range(20):
        width -= 10
        height += 10
        r -= 10
        g += 10
        rect = Rect((0,0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r, g, b))

pgzrun.go()

