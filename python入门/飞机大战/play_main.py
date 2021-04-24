#! /usr/bin/python3
import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        print("游戏初始化...")
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)

    def __create_sprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            print("game over")
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
