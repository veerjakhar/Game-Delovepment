import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 600
score = 0

masseage = "Pollinate... or else"
bee = Actor('bee.png')
bee.pos = 100,100
flower = Actor('flower.png')
flower.pos = 200, 200


def draw():
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: " + str(score), color = "black", topleft = (10,10))

def place_flower():
    flower.x =  randint(70, (WIDTH  - 70))
    flower.y = randint(70, (HEIGHT - 70))

def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 2
    elif keyboard.right:
        bee.x = bee.x + 2
    elif keyboard.up:
        bee.y = bee.y - 2
    elif keyboard.down:
        bee.y = bee.y + 2
    
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score += 10
        place_flower()
   



pgzrun.go()
