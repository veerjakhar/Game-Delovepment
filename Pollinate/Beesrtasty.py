import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 600
score = 0
game_over = False

message = "Pollinate... or else"
bee = Actor('bee.png')
bee.pos = 100,100
flower = Actor('flower.png')
flower.pos = 200, 200


def draw():
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: " + str(score), color = "black", topleft = (10,10))
    if game_over == True:
        screen.draw.text("Time is up your final score is: " + str(score), color = "black", midtop = (WIDTH/2, 10), fontsize = 40)
def place_flower():
    flower.x =  randint(70, (WIDTH  - 70))
    flower.y = randint(70, (HEIGHT - 70))

def time_up():
    global game_over
    game_over = True

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
   
clock.schedule(time_up, 10)
pgzrun.go()
