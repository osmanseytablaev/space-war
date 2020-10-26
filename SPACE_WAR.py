import pygame
import random
class Ship:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (0, 77, 255),
                         pygame.Rect(self.x, self.y, 100, 75))
class Bullet:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (254, 52, 110), 
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 5 
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
        ship = Ship(self, 450, 600)
        bullet = None
        while True:
            ship.draw()
            pygame.display.flip()
            self.screen.fill((0, 0, 0))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  
                ship.x -= 2 if ship.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                ship.x += 2 if ship.x < W - 20 else 0
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit() 
                if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                    self.bullets.append(Bullet(self, ship.x, ship.y))
            for bullet in self.bullets:
                bullet.draw()
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