import pygame
import random
from pygame.locals import *
pygame.init()
W = 900
H = 700
space_x = 450
space_y = 600
enemyX = random.randint(1, 900)
enemyY = 0.99
pygame.display.set_caption("SPACE WAR")
display_surface = pygame.display.set_mode((W, H))
shoot = pygame.image.load('shoot.jpg')
bullet_state = "ready"
class Space:
    def __init__(self, position_x, position_y):    
        self.position_x = position_x
        self.position_y = position_y
        self.bulletX = self.position_x
        self.bulletY = self.position_y
    def show(self):
        space = pygame.draw.rect(display_surface, (255, 255, 255), (self.position_x, self.position_y, 100, 75))
    def fire(self):
        display_surface.blit(shoot, (self.bulletX, self.bulletY))
        self.bulletX = self.position_x
        self.bulletY -= 10
        print(self.bulletY)
        clock.tick(60)
space = Space(450, 600)
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:    
            if i.key == pygame.K_LEFT:
                space.position_x -= 10 if space.position_x > 20 else 0
            if i.key == pygame.K_RIGHT:
                space.position_x += 10 if space.position_x < W - 20 else 0
            if i.key == pygame.K_SPACE:
                bullet_state = "fire"
    clock = pygame.time.Clock()
    enemy = pygame.image.load('enemy.jpg')
    display_surface.blit(enemy, (enemyX, enemyY))
    pygame.display.update()
    display_surface.fill((0,0,0))
    enemyY += 0.50
    if bullet_state == "fire":
        space.fire()
    space.show()
#Моя проблема была в том что когда я писал движение пули в
#if событии оно у меня не выполнялось бесконечно тоесть в while
#решение: создать переменную с любым значением
#и изменить значение в событии и потом в while пишем если
#переменная равно тому значению то выполняем наш код





