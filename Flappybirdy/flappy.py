import pygame

pygame.init()

WIDTH = 864
HEIGHT = 536

clock = pygame.time.Clock()
fps = 60

ground_scroll = 0
scroll_speed = 4

Screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Flappy Bird')

bird_img = pygame.image.load('flappybird.png')
Screen.blit(bird_img, (10, 10))

pygame.display.update()

Run = True

while Run:
    clock.tick(fps)
    Screen.blit(pygame.image.load("backg.png"), (0, -200))
    bird_img = pygame.image.load('flappybird.png')
    Screen.blit(bird_img, (30, 200))
    ground_img = pygame.image.load('ground.png')
    Screen.blit(ground_img, (ground_scroll, 418))
    ground_scroll = ground_scroll - scroll_speed

    if ground_scroll <- 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            pygame.quit()
    pygame.display.update()