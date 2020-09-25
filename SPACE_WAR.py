import pygame
import rx
import random
from pygame.locals import *
W = 900
H = 700
YELLOW = (225, 225, 0)
space_x = 450
space_y = 600
enemyX = random.randint(1, 900)
enemyY = 20 
pygame.init()
pygame.display.set_caption("SPACE WAR")
display_surface = pygame.display.set_mode((W, H))
shoot = pygame.image.load('shoot.jpg')
bulletX = space_x
bulletY = 600
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
def fire_bullet():
    display_surface.blit(shoot, (bulletX, bulletY))    
while True:
    clock = pygame.time.Clock()
    enemy = pygame.image.load('enemy.jpg')
    display_surface.blit(enemy, (enemyX, enemyY))
    pygame.display.update()
    display_surface.fill((0,0,0))
    enemyY += 0.50
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                display_surface.fill((0,0,0))
                space_x -= 10 if space_x > 20 else 0
            if i.key == pygame.K_RIGHT:
                display_surface.fill((0,0,0))
                space_x += 10 if space_x < W - 20 else 0
            if i.key == pygame.K_SPACE:
                bullet_state = "fire"
    if bullet_state == "fire":
        fire_bullet()
        bulletY -= 10
        print(bulletY)
        clock.tick(60)
        if bulletY == 0:
            bullet_state = "ready"
    space = pygame.draw.rect(display_surface, (255, 255, 255), (space_x, space_y, 100, 75))           
#Моя проблема была в том что когда я писал движение пули в
#if событии оно у меня не выполнялось бесконечно тоесть в while
#решение: создать переменную с любым значением
#и изменить значение в событии и потом в while пишем если
#переменная равно тому значению то выполняем наш код
