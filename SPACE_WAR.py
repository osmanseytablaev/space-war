import pygame
import random
import time

import self as self


class Ship:
    def __init__(self, game1, ship_x, ship_y):
        self.ship_x = ship_x
        self.ship_y = ship_y
        self.game = game1
        self.gun_x = self.ship_x + 24
        self.gun_y = self.ship_y

    def show(self):
        self.gun_x = self.ship_x
        self.gun_y = self.ship_y
        ship = pygame.image.load('ship.png')
        self.game.screen.blit(ship, (self.ship_x, self.ship_y))

    def fire(self):
        pygame.draw.rect(self.game.screen,
                         (254, 52, 110),
                         pygame.Rect(self.gun_x, self.gun_y, 2, 4))
        self.gun_y -= 5


class Enemy:
    def __init__(self, game1, enemy_x, enemy_y):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.game = game1

    def attack(self):
        enemy = pygame.image.load('enemy.png')
        self.game.screen.blit(enemy, (self.enemy_x, self.enemy_y))
        self.enemy_y += 0.20

class Game:
    bullets = []
    enemies = []

    def check_exit(self):
        current_time = time.clock()
        print(current_time)
        if current_time >= 5:
            return True
        else:
            return False
    def __init__(self, w, h):
        pygame.init()
        self.w = w
        self.h = h
        pygame.display.set_caption("SPACE wAR")
        self.screen = pygame.display.set_mode((w, h))
        bullet = None
        ship = Ship(self, 450, 650)
        enemy = Enemy(self, random.randint(1, 900), 0.99)
        self.start_time = 0
        game =  True
        while game == True:
            if self.check_exit():
                print('Game end')
                break
            ship.show()
            enemy.attack()
            pygame.display.flip()
            self.screen.fill((0, 0, 0))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                ship.ship_x -= 2 if ship.ship_x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                ship.ship_x += 2 if ship.ship_x < self.w - 20 else 0
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                    self.bullets.append(Ship(self, ship.gun_x, ship.gun_y))
            for bullet in self.bullets:
                bullet.fire()


if __name__ == '__main__':
    game = Game(900, 700)
# Проблема-1
# Моя проблема была в том что когда я писал движение пули в
# if событии оно у меня не выполнялось бесконечно тоесть в while
# Решение: создать переменную с любым значением
# и изменить значение в событии и потом в while пишем если
# переменная равно тому значению то выполняем наш код


# Проблема-2
# Когда я писал несколько пуль и все остальное у меня ничего не поэвлялось
# Дело в том что когда я рисую спрайты *на pygame* мне нужно обновлять екран
# Решение: добавить метод display.flip()
