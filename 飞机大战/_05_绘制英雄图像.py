import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
screen.blit(background, (0, 0))
screen.blit(hero, (200, 500))

pygame.display.update()

while True:
    pass

pygame.quit()
