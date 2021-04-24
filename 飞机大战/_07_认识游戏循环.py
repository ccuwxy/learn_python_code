import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
screen.blit(background, (0, 0))
screen.blit(hero, (200, 500))

pygame.display.update()

clock = pygame.time.Clock()
i = 0
while True:
    clock.tick(60)
    pygame.display.update()
    i += 1
    print(i)

pygame.quit()
