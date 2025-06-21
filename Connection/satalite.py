import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
num_of_satellites = 8
satellites = []
lines = []

def create_satellites():
    for i in range(num_of_satellites):
        satellite = Actor('satelite.png')
        satellite.pos = randint(40, WIDTH - 40), randint(40, HEIGHT - 40)
        satellites.append(satellite)

def draw():
    number = 1
    screen.blit('space', (0,0))
    for sat in satellites:
        sat.draw()
        screen.draw.text(str(number), (sat.pos[0], sat.pos[1] + 20))
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 0, 0))

create_satellites()
pgzrun.go()
