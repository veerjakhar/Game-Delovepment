import pgzrun
import random

current_level = 1
game_over = False
game_complete = False
START_SPEED = 10
FINAL_LEVEL = 6

WIDTH = 600
HEIGHT = 800
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)

ITEMS = ["battery", "bottle", "plastic", "chips"]
animations = []
items = []

def draw():
    global items, game_over, game_complete, current_level
    screen.clear()
    screen.blit("background", (0,0))
    if game_over:
        display_message("Game Over", "Try Again")
    elif game_complete:
        display_message("You won", "Well Done")
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

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def  handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animation(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animation(animations_to_stop):
    for animations in animations_to_stop:
        if animations.running:
            animations.stop()

def handle_game_over():
    global game_over
    game_over = True

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize = 60, center = CENTER, color = "black")
    screen.draw.text(sub_heading_text, fontsize = 30, center =(CENTER_X, CENTER_Y + 30), color = "black") 



pgzrun.go()