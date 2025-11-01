import pygame

pygame.init()

pygame.display.set_caption("Rocket in Space")

WIDTH = 600
HEIGHT = 600

Screen = pygame.display.set_mode([WIDTH, HEIGHT])
Screen.blit(pygame.image.load("background.png"), (0, 0))

pygame.display.update()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()

    def update(self, press_key):
        if press_key[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if press_key[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if press_key[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        if press_key[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)

Player1 = Player()
Sprites = pygame.sprite.Group()
Sprites.add(Player1)

while True:
    Sprites.draw(Screen)
    press_key = pygame.key.get_pressed()
    Player1.update(press_key)
    pygame.display.update()