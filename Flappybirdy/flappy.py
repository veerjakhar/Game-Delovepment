import pygame
from pygame.locals import *
import random

pygame.init()

WIDTH = 864
HEIGHT = 536

pipe_gap = 150
pipe_freq = 1500

last_pipe = pygame.time.get_ticks()

score = 0
pass_pipe = False

clock = pygame.time.Clock()
fps = 606

font = pygame.font.SysFont('Bauhaus 93', 60)
white = (255, 255, 255)

ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False

Screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Flappy Bird')

button_img = pygame.image.load('buttonimg.png')

pygame.display.update()

Run = True

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    Screen.blit(img, (x, y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(HEIGHT / 2)
    score = 0
    return score

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        img1 = pygame.image.load('flappybird.png')
        img2 = pygame.image.load('flappybirdimg2.png')
        img3 = pygame.image.load('flappybirdimg3.png')
        self.images = [img1, img2, img3]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.click = False

    def update(self):
        if flying == True:
            # Gravity
            self.vel += 0.2
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        if game_over == False:
            # Jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -8
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # Handle Animations
            self.counter = self.counter + 1
            flap_cooldown = 5
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index = self.index + 1
                if self.index >= len(self.images):
                    self.index = 0
                    self.image = self.images[self.index]

                    # Rotate The Bird
                    self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()

        # Position 1 is from top and -1 is from bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x = self.rect.x - scroll_speed
        if self.rect.right < 0 :
            self.kill()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False

        # Get Mouse Position
        pos = pygame.mouse.get_pos()

        # Check If Mouse Is Over The Button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        # Draw Button
        Screen.blit(self.image, self.rect.x, self.rect.y)
        return action

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100, int(HEIGHT / 2))
bird_group.add(flappy)
#flappy3 = Bird(150, int(HEIGHT / 2 + 40))
#bird_group.add(flappy3)

# Create Restart Button
button = Button(WIDTH // 2 - 50, HEIGHT // 2 - 100, button_img)

while Run:
    clock.tick(fps)
    Screen.blit(pygame.image.load("backg.png"), (0, -200))
    bird_group.draw(Screen)
    pipe_group.draw(Screen)
    bird_group.update()

    ground_img = pygame.image.load('ground.png')
    Screen.blit(ground_img, (ground_scroll, 418))

    # Check The Score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False:
            pass_pipe = True

        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score = score + 1
                pass_pipe = False
            
    draw_text(str(score), font, white, int(WIDTH / 2), 20)

    # Look For Collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
        game_over = True


    # Check If The Bird Has Hit The Ground
    if flappy.rect.bottom >= 420:
        game_over = True
        flying = False

    if game_over == False and flying == True:
        # Genterate New Pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_freq:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(WIDTH, int(HEIGHT / 2) + HEIGHT, -1)
            top_pipe = Pipe(WIDTH, int(HEIGHT / 2) + HEIGHT, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        ground_scroll = ground_scroll - scroll_speed
        if ground_scroll <- 35:
            ground_scroll = 0

        pipe_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    pygame.display.update()
pygame.quit()