import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load("python入门/飞机大战/images/background.png")

screen.blit(background, (0, 0))

pygame.display.update()

while True:
    pass

pygame.quit()
