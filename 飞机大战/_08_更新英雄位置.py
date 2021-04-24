import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
screen.blit(background, (0, 0))
# screen.blit(hero, (200, 500))

hero_rect = pygame.Rect(200, 500, 102, 126)
pygame.display.update()

clock = pygame.time.Clock()

while True:
    clock.tick(120)
    hero_rect.y -= 1
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()

pygame.quit()
