import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load("python入门/飞机大战/images/background.png")
hero = pygame.image.load("python入门/飞机大战/images/me1.png")
screen.blit(background, (0, 0))
# screen.blit(hero, (200, 500))

hero_rect = pygame.Rect(200, 500, 102, 126)
pygame.display.update()

clock = pygame.time.Clock()

while True:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()

    if hero_rect.y <= -126:
        hero_rect.y = 700
    hero_rect.y -= 1
    screen.blit(background, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()


