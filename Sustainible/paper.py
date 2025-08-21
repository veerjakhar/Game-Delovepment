import pgzrun
import random

current_level = 1
game_over = False
game_complete = False
START_SPEED = 10

WIDTH = 600
HEIGHT = 800
Centerx = WIDTH / 2
Centery = HEIGHT / 2
Center = (Centerx, Centery)

ITEMS = ["battery", "bottle", "plasic", "chips"]
animations = []
items = []

def draw():
    global items, game_over, game_complete, current_level
    screen.clear()
    screen.blit("background", (0,0))
    if game_over:
        display_message("Game Over", "Try Again")
    elif game_complete:
        display_message("You won")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    for i in range(0,number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    newitems = []
    for options in items_to_create:
        item = Actor(options + "img")
        newitems.append(item)
    return newitems

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    for i, item in enumerate(items_to_layout):
        new_xpos = (i + 1) * gap_size
        item.x = new_xpos 

def animate_items(items_to_animate):  
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ("center", "bottom")
        animation = animate(item, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True




pgzrun.go()