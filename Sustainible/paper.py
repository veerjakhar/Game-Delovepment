import pgzrun

current_level = 1
game_over = False
game_complete = False

WIDTH = 600
HEIGHT = 800
Centerx = WIDTH / 2
Centery = HEIGHT / 2
Center = (Centerx, Centery)

items = ["battery", "bottle", "plasic", "chips"]


def draw():
    screen.blit("background", (0,0))
    if game_over:
        display_message("Game Over", "Try Again")
    elif game_complete:
        display_message("You won")
    else:
        for item in items:
            item.draw()

def create_items(items_to_create):
    newitems = []
    for options in items_to_create:
        item = Actor(option + "img")
        newitems.append(item)
    return newitems

pgzrun.go()