import pygame
from pygame.locals import *
import time
import random

pygame.init()

WIDTH = 900
HEIGHT = 700

score = 0
red = (255, 0, 0)
white = (255, 255, 255)


pygame.display.set_caption('Recycle Marathon')

def change_background(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background, (WIDTH, HEIGHT))
    Screen.blit(bg, (0, 0))

Screen = pygame.display.set_mode([WIDTH, HEIGHT])

playing = True
clock = pygame.time.Clock()
start_time = time.time()

# Font to Print Scores on Screen
my_font = pygame.font.SysFont("Times New Roman", 22)
timing_font = pygame.font.SysFont("Times New Roman", 22)
text = my_font.render("Score = " + str(0), True, white)

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()

class Recycled(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

class NonRecycled(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bag.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()

images = ["item1.png", "item2.png", "item3.png"]
item_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()

# Create Item Sprites
for i in range (50):
    item = Recycled(random.choice(images))
    # Set a random location for the item
    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    item_list.add(item)
    all_sprites.add(item)

# Create Plastic
for i in range (20):
    plastic = NonRecycled()
    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.y = random.randrange(HEIGHT)
    all_sprites.add(plastic) 
    plastic_list.add(plastic)

bin = Bin()
all_sprites.add(bin)

while playing:
    # This is used to control the speed
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # Check if time is greater that 60 seconds
    time_left = time.time() - start_time
    if time_left >= 60:
        if score > 50:
            text = my_font.render(" Bin Loot Sucessfull ", True, red)
            change_background("winscreen.jpeg")
        else:
            text = my_font.render(" Better Luck Next Time ", True, white)
            change_background("losescreen.jpg")
        Screen.blit(text, (250, 40))
    else:
        change_background("bg.png")
        countdown = timing_font.render("Time left: " + str(60 - int(time_left)), True, white)
        Screen.blit(countdown, (20, 10))

        # Move the Glove as per Key Pressed
        keys = pygame.key.get_pressed()
        if keys [pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5

        if keys[pygame.K_DOWN]:
            if bin.rect.y < 630:
                bin.rect.y += 5

        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5

        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 850:
                bin.rect.x += 5

        # See if Item and Bin have Collided
        item_hit_list = pygame.sprite.spritecollide(bin, item_list, True)
        plastic_hit_list = pygame.sprite.spritecollide(bin, plastic_list, True)

        # Check the List of Collitions
        for item in item_hit_list:
            score = score + 1
            text = my_font.render("Score = " + str(score), True, white)
        for plastic in plastic_hit_list:
            score = score - 1
            text = my_font.render("Score = " + str(score), True, white)


        # Print the Score on Screen
        Screen.blit(text, (20, 50))

        # Draw all Sprites
        all_sprites.draw(Screen)
    pygame.display.update()