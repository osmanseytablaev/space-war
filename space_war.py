import pygame
import random
import datetime as dt
import time


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
        ship = pygame.image.load('images/ship.png')
        self.game.screen.blit(ship, (self.ship_x, self.ship_y))

    def fire(self):
        pygame.draw.rect(self.game.screen,
                         (254, 52, 110),
                         pygame.Rect(self.gun_x, self.gun_y, 2, 4))
        self.gun_y -= 1


class Enemy:
    def __init__(self, game1, enemy_x, enemy_y):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.game = game1
        self.size = 40

    def show(self):
        enemy = pygame.image.load('images/enemy.png')
        self.game.screen.blit(enemy, (self.enemy_x, self.enemy_y))
        self.enemy_y += 0.45

    def el_destroyer0_0(self, game):
        for bullet in game.bullets:
            if (self.enemy_x + self.size > bullet.gun_x > self.enemy_x - self.size and
                    self.enemy_y + self.size > bullet.gun_y > self.enemy_y - self.size):
                game.bullets.remove(bullet)
                game.enemies.remove(self)
                return True

    def des(self, game):
        if self.enemy_y >= 700:
            game.enemies.remove(self)
            return True


class Enemy2:
    def __init__(self, game1, enemy_x, enemy_y):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.game = game1
        self.size = 40

    def show(self):
        enemy = pygame.image.load('images/enemy.png')
        self.game.screen.blit(enemy, (self.enemy_x, self.enemy_y))
        self.enemy_y += 0.50

    def el_destroyer0_0(self, game):
        for bullet in game.bullets:
            if (self.enemy_x + self.size > bullet.gun_x > self.enemy_x - self.size and
                    self.enemy_y + self.size > bullet.gun_y > self.enemy_y - self.size):
                game.bullets.remove(bullet)
                game.enemies.remove(self)
                return True

    def des(self, game):
        if self.enemy_y >= 700:
            game.enemies.remove(self)
            return True


class Enemy3:
    def __init__(self, game1, enemy_x, enemy_y):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.game = game1
        self.size = 40

    def show(self):
        enemy = pygame.image.load('images/enemy.png')
        self.game.screen.blit(enemy, (self.enemy_x, self.enemy_y))
        self.enemy_y += 1

    def el_destroyer0_0(self, game):
        for bullet in game.bullets:
            if (self.enemy_x + self.size > bullet.gun_x > self.enemy_x - self.size and
                    self.enemy_y + self.size > bullet.gun_y > self.enemy_y - self.size):
                game.bullets.remove(bullet)
                game.enemies.remove(self)
                return True

    def des(self, game):
        if self.enemy_y >= 700:
            game.enemies.remove(self)
            return True


class Game:
    ships = []
    bullets = []
    enemies = []

    def check_exit(self):
        date_game = dt.datetime.now() - self.time_game
        if date_game.seconds >= 180:  # 60 * 3 = 180 sec = 3 min game
            return True
        else:
            return False

    def __init__(self, w, h):  # Constructor
        pygame.init()
        print("Это игра Space War тут 3 уровня. Удачи!")
        pygame.mixer.init()
        pygame.mixer.music.load('audio/start.ogg')
        pygame.mixer.music.play()
        self.w = w
        self.h = h
        pygame.display.set_caption("Space War")
        self.screen = pygame.display.set_mode((w, h))
        ship = Ship(self, 240, 650)
        enemy1 = Enemy(self, random.randint(1, 400), 0.99)
        enemy2 = Enemy2(self, random.randint(1, 400), 0.99)
        enemy3 = Enemy3(self, random.randint(1, 400), 0.99)
        self.time = dt.datetime.now()
        self.time_game = dt.datetime.now()
        self.score_value = 0
        self.score_need1 = 20
        self.score_need2 = 30
        self.score_need3 = 40
        self.life = 3
        self.YELLOW = 255, 255, 0
        while True:
            ship.show()
            pygame.init()
            f7 = pygame.font.SysFont('serif', 20)
            text7 = f7.render("LEVEL 1", True,
                              self.YELLOW)
            self.screen.blit(text7, (420, 20))
            if self.check_exit():
                print('Game end')
                break
            date = dt.datetime.now() - self.time
            if date.seconds >= 3:
                self.enemies.append(Enemy(self, random.randint(1, 400), enemy1.enemy_y))
                self.time = dt.datetime.now()
            f1 = pygame.font.SysFont('serif', 20)
            text1 = f1.render("Score: " + str(self.score_value), True,
                              self.YELLOW)
            self.screen.blit(text1, (420, 670))
            f2 = pygame.font.SysFont('serif', 20)
            text2 = f2.render("Life: " + str(self.life), True,
                              self.YELLOW)
            self.screen.blit(text2, (420, 650))
            pygame.display.flip()
            self.screen.fill((0, 0, 0))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                ship.ship_x -= 0.50 if ship.ship_x > 0 else 0
            elif pressed[pygame.K_RIGHT]:
                ship.ship_x += 0.50 if ship.ship_x < self.w - 50 else 0
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                    self.bullets.append(Ship(self, ship.gun_x, ship.gun_y))
                    pygame.mixer.music.load("audio/laser.ogg")
                    pygame.mixer.music.play()
            if self.life == 0:
                f3 = pygame.font.SysFont('serif', 45)
                text3 = f3.render("GAME OVER", True,
                                  (255, 0, 0))
                self.screen.blit(text3, (150, 300))
                pygame.mixer.music.load("audio/fail.ogg")
                pygame.mixer.music.play()
                if date.seconds >= 2:
                    time.sleep(3)
                    exit()
            if self.score_value == 20:
                f4 = pygame.font.SysFont('serif', 45)
                text4 = f4.render("YOU WON!", True,
                                  (0, 255, 0))
                self.screen.blit(text4, (150, 300))
                pygame.mixer.music.load("audio/game-won.ogg")
                pygame.mixer.music.play()
                if date.seconds >= 2:
                    time.sleep(3)
                    while True:
                        f5 = pygame.font.SysFont('serif', 45)
                        text5 = f5.render("LEVEL 2", True,
                                          self.YELLOW)
                        self.screen.blit(text5, (420, 20))
                        self.life = 3
                        self.score_value = 0
                        if self.check_exit():
                            print('Game end')
                            break
                        date = dt.datetime.now() - self.time
                        if date.seconds >= 2:
                            self.enemies.append(Enemy2(self, random.randint(1, 400), enemy2.enemy_y))
                            self.time = dt.datetime.now()
                        f1 = pygame.font.SysFont('serif', 20)
                        text1 = f1.render("Score: " + str(self.score_value), True,
                                          self.YELLOW)
                        self.screen.blit(text1, (420, 670))
                        f2 = pygame.font.SysFont('serif', 20)
                        text2 = f2.render("Life: " + str(self.life), True,
                                          self.YELLOW)
                        self.screen.blit(text2, (420, 650))
                        ship.show()
                        pygame.display.flip()
                        self.screen.fill((0, 0, 0))
                        pressed = pygame.key.get_pressed()
                        if pressed[pygame.K_LEFT]:
                            ship.ship_x -= 0.50 if ship.ship_x > 0 else 0
                        elif pressed[pygame.K_RIGHT]:
                            ship.ship_x += 0.50 if ship.ship_x < self.w - 50 else 0
                        for i in pygame.event.get():
                            if i.type == pygame.QUIT:
                                exit()
                            if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                                self.bullets.append(Ship(self, ship.gun_x, ship.gun_y))
                                pygame.mixer.music.load("audio/laser.ogg")
                                pygame.mixer.music.play()
                        if self.life == 0:
                            f3 = pygame.font.SysFont('serif', 45)
                            text3 = f3.render("GAME OVER", True,
                                              (255, 0, 0))
                            self.screen.blit(text3, (150, 300))
                            pygame.mixer.music.load("audio/fail.ogg")
                            pygame.mixer.music.play()
                            if date.seconds >= 2:
                                time.sleep(3)
                                exit()
                        if self.score_value == 30:
                            f4 = pygame.font.SysFont('serif', 45)
                            text4 = f4.render("YOU GOOD!", True,
                                              (0, 255, 0))
                            self.screen.blit(text4, (150, 300))
                            pygame.mixer.music.load("audio/game-won.ogg")
                            pygame.mixer.music.play()
                            if date.seconds >= 2:
                                time.sleep(3)
                                while True:
                                    f6 = pygame.font.SysFont('serif', 20)
                                    text6 = f6.render("LEVEL 3", True,
                                                      self.YELLOW)
                                    self.screen.blit(text6, (420, 20))
                                    self.life = 2
                                    self.score_value = 0
                                    if self.check_exit():
                                        print('Game end')
                                        break
                                    date = dt.datetime.now() - self.time
                                    if date.seconds >= 2:
                                        self.enemies.append(Enemy3(self, random.randint(1, 400), enemy3.enemy_y))
                                        self.time = dt.datetime.now()
                                    f1 = pygame.font.SysFont('serif', 20)
                                    text1 = f1.render("Score: " + str(self.score_value), True,
                                                      self.YELLOW)
                                    self.screen.blit(text1, (420, 670))
                                    f2 = pygame.font.SysFont('serif', 20)
                                    text2 = f2.render("Life: " + str(self.life), True,
                                                      self.YELLOW)
                                    self.screen.blit(text2, (420, 650))
                                    ship.show()
                                    pygame.display.flip()
                                    self.screen.fill((0, 0, 0))
                                    pressed = pygame.key.get_pressed()
                                    if pressed[pygame.K_LEFT]:
                                        ship.ship_x -= 0.50 if ship.ship_x > 0 else 0
                                    elif pressed[pygame.K_RIGHT]:
                                        ship.ship_x += 0.50 if ship.ship_x < self.w - 50 else 0
                                    for i in pygame.event.get():
                                        if i.type == pygame.QUIT:
                                            exit()
                                        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                                            self.bullets.append(Ship(self, ship.gun_x, ship.gun_y))
                                            pygame.mixer.music.load("audio/laser.ogg")
                                            pygame.mixer.music.play()
                                    if self.life == 0:
                                        f3 = pygame.font.SysFont('serif', 45)
                                        text3 = f3.render("GAME OVER", True,
                                                          (255, 0, 0))
                                        self.screen.blit(text3, (150, 300))
                                        pygame.mixer.music.load("audio/fail.ogg")
                                        pygame.mixer.music.play()
                                        if date.seconds >= 2:
                                            time.sleep(3)
                                            exit()
                                    if self.score_value == 40:
                                        f4 = pygame.font.SysFont('serif', 45)
                                        text4 = f4.render("YOU MASTER SPACE WAR!", True,
                                                          (0, 255, 0))
                                        self.screen.blit(text4, (150, 300))
                                        pygame.mixer.music.load("audio/game-won.ogg")
                                        pygame.mixer.music.play()
                                        if date.seconds >= 2:
                                            time.sleep(3)
                                            exit()
                                    for bullet in self.bullets:
                                        bullet.fire()
                                    for enemy_state in self.enemies:
                                        enemy_state.show()
                                        if enemy_state.el_destroyer0_0(self):
                                            self.score_value += 1
                                            self.screen.blit(text1, (420, 670))
                                    for enemy_st in self.enemies:
                                        if enemy_st.des(self):
                                            self.life -= 1
                                            self.screen.blit(text2, (420, 650))
                        for bullet in self.bullets:
                            bullet.fire()
                        for enemy_state in self.enemies:
                            enemy_state.show()
                            if enemy_state.el_destroyer0_0(self):
                                self.score_value += 1
                                self.screen.blit(text1, (420, 670))
                        for enemy_st in self.enemies:
                            if enemy_st.des(self):
                                self.life -= 1
                                self.screen.blit(text2, (420, 650))
            for bullet in self.bullets:
                bullet.fire()
            for enemy_state in self.enemies:
                enemy_state.show()
                if enemy_state.el_destroyer0_0(self):
                    self.score_value += 1
                    self.screen.blit(text1, (420, 670))
            for enemy_st in self.enemies:
                if enemy_st.des(self):
                    self.life -= 1
                    self.screen.blit(text2, (420, 650))


if __name__ == '__main__':
    Game(500, 700)
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
