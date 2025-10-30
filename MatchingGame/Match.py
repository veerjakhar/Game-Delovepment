import pygame

pygame.init()


Screen = pygame.display.set_mode((600, 600))
Screen.fill((255, 255, 255))

font = pygame.font.SysFont('comicsans', 40)
text = font.render("Ludo", True, (0, 0, 0))
text2 = font.render("CandyCrush", True, (0, 0, 0))
text3 = font.render("Subway Surfers", True, (0, 0, 0))
text4 = font.render("Temple Run", True, (0, 0, 0))

Ludo = pygame.image.load("Ludo.png")
Candy = pygame.image.load("Candy.jpg")
Subway = pygame.image.load("Subway.png")
Temple = pygame.image.load("Temple.png")

Screen.blit(text, (275, 400))
Screen.blit(text2, (275, 300))
Screen.blit(text3, (275, 200))
Screen.blit(text4, (275, 100))

Screen.blit(Ludo, (150, 200))
Screen.blit(Candy, (150, 400))
Screen.blit(Subway, (150, 100))
Screen.blit(Temple, (150, 300))
pygame.display.update()

while 1:
    pygame.display.update()
    event = pygame.event.poll()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos1 = pygame.mouse.get_pos()
        pygame.draw.circle(Screen, (111, 230, 67), (pos1), 10, 0)
        pygame.display.update()

    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.circle(Screen, (0, 0, 0), (pos2), 10, 0)
        pygame.draw.line(Screen, (0, 0, 0), (pos1), (pos2), 5)
        pygame.display.update()

    if event.type == pygame.QUIT:
        Run = False
        pygame.quit()