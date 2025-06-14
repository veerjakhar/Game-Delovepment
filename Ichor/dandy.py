import pgzrun
from random import randint

HEIGHT = 400
WIDTH = 405
score = 0
twisted = False

dandy = Actor("dandy.png")
dandy.pos = 100, 100
ichor = Actor("ichor.png")
ichor.pos = 200, 200

def draw():
    screen.blit("fakedw", (0,0))
    dandy.draw()
    ichor.draw()
    screen.draw.text("Score: " + str(score), color = ("black"), topleft = (10, 10))
    if twisted == True:
        screen.draw.text("Your final score is: " + str(score), color = ("black"), midtop = (WIDTH/2, 10), fontsize = 40)

def gtg():
    global twisted
    twisted = True


def machine():
    ichor.x = randint(70, (WIDTH - 70))
    ichor.y = randint(70, (HEIGHT - 70))

def move():
    if keyboard.left:
        ichor.x = ichor.x - 2
    elif keyboard.right:
        ichor.x = ichor.x + 2
    elif keyboard.up:
        ichor.y = ichor.y + 2
    elif keyboard.down:
        ichor.y = ichor.y - 2

    ichor_col = ichor.colliderect(flower)
    if ichor_col:
        score += 10
        machine()

clock.schedule(gtg, 10)
pgzrun.go()