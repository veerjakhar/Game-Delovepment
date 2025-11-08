import pygame

pygame.init()

WIDTH = 864
HEIGHT = 536

clock = pygame.time.Clock()
fps = 60

ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False

Screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Flappy Bird')

pygame.display.update()

Run = True

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
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)
        if game_over == False:
            # Jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
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

bird_group = pygame.sprite.Group()
flappy = Bird(100, int(HEIGHT / 2))
bird_group.add(flappy)


while Run:
    clock.tick(fps)
    Screen.blit(pygame.image.load("backg.png"), (0, -200))
    bird_group.draw(Screen)
    bird_group.update()

    ground_img = pygame.image.load('ground.png')
    Screen.blit(ground_img, (ground_scroll, 418))

    # Check If The Bird Has Hit The Ground
    if flappy.rect.bottom > 768:
        game_over = True
        flying = False

    if game_over == False:
        ground_scroll = ground_scroll - scroll_speed
        if ground_scroll <- 35:
            ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    pygame.display.update()
pygame.quit()