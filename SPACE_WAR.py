import pygame
import random
YELLOW = (225, 225, 0)
class Ship:
    def __init__(self, game, ship_x, ship_y):
        self.ship_x = ship_x
        self.ship_y = ship_y
        self.game = game
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
class Game:
    bullets = []
    bullet_state = "ready"
    enemyX = random.randint(1, 900)
    enemyY = 0.99
    def __init__(self, W, H):
        pygame.init()
        self.W = W
        self.H = H
        pygame.display.set_caption("SPACE WAR")
        self.screen = pygame.display.set_mode((W, H))
        bullet = None
        ship = Ship(self, 450, 650)
        while True:
            ship.show()
            pygame.display.flip()
            self.screen.fill((0, 0, 0))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  
                ship.ship_x -= 2 if ship.ship_x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                ship.ship_x += 2 if ship.ship_x < W - 20 else 0
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit() 
                if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                    self.bullets.append(Ship(self, ship.gun_x, ship.gun_y))
            for bullet in self.bullets:
                bullet.fire()
if __name__ == '__main__':
    game = Game(900, 700)
#Проблема-1
#Моя проблема была в том что когда я писал движение пули в
#if событии оно у меня не выполнялось бесконечно тоесть в while
#Решение: создать переменную с любым значением
#и изменить значение в событии и потом в while пишем если
#переменная равно тому значению то выполняем наш код


#Проблема-2
#Когда я писал несколько пуль и все остальное у меня ничего не поэвлялось
#Дело в том что когда я рисую спрайты *на pygame* мне нужно обновлять екран
#Решение: добавить метод display.flip()