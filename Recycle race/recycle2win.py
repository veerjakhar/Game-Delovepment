import pygame
import time
import random

pygame.init()

WIDTH = 900
HEIGHT = 700

pygame.display.set_caption('Recycle Marathon')

def change_background(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background ,(WIDTH, HEIGHT))
    Screen.blit(bg, (0, 0))

Screen = pygame.display.set_mode([WIDTH, HEIGHT])

playing = True
clock = pygame.time.Clock()

while playing:
    # This is used to control the speed
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    change_background('bg.png')
    pygame.display.update()