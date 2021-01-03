import pygame
import random
import datetime as dt


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
        self.size = 40

    def show(self):
        enemy = pygame.image.load('enemy.png')
        self.game.screen.blit(enemy, (self.enemy_x, self.enemy_y))
        self.enemy_y += 0.20

    def el_destroyer0_0(self, game):
        for bullet in game.bullets:
            if (self.enemy_x + self.size > bullet.gun_x > self.enemy_x - self.size and
                    self.enemy_y + self.size > bullet.gun_y > self.enemy_y - self.size):
                game.bullets.remove(bullet)
                game.enemies.remove(self)
                pygame.mixer.music.load('boom2.mp3')
                pygame.mixer.music.play()
                return True


class Game:
    bullets = []
    enemies = []

    def check_exit(self):
        date_game = dt.datetime.now() - self.time_game
        if date_game.seconds >= 300:  # 60 * 5 = 300 sec = 5 min game
            return True
        else:
            return False

    def __init__(self, w, h):
        pygame.init()
        pygame.mixer.music.load('A4.mp3')
        pygame.mixer.music.play()
        self.w = w
        self.h = h
        pygame.display.set_caption("SPACE WAR")
        self.screen = pygame.display.set_mode((w, h))
        ship = Ship(self, 450, 650)
        enemy = Enemy(self, random.randint(1, 500), 0.99)
        self.time = dt.datetime.now()
        self.time_game = dt.datetime.now()
        self.score_value = 0
        self.YELLOW = 255, 255, 0
        while True:
            if self.check_exit():
                print('Game end')
                break
            date = dt.datetime.now() - self.time
            if date.seconds >= 5:
                self.enemies.append(Enemy(self, random.randint(1, 800), enemy.enemy_y))
                self.time = dt.datetime.now()
            f1 = pygame.font.SysFont('serif', 16)
            text1 = f1.render("Score:" + str(self.score_value), True,
                              self.YELLOW)
            self.screen.blit(text1, (820, 670))
            ship.show()
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
                    pygame.mixer.music.load('boom.mp3')
                    pygame.mixer.music.play()
            for bullet in self.bullets:
                bullet.fire()
            for enemy_state in self.enemies:
                enemy_state.show()
                if enemy_state.el_destroyer0_0(self):
                    self.score_value += 1
                    self.screen.blit(text1, (820, 670))


if __name__ == '__main__':
    Game(900, 700)
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
