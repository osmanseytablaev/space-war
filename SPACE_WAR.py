import pygame
import time
from pygame.locals import *
W = 900
H = 700
YELLOW = (225, 225, 0)
x = 450
y = 650
y2 = 650
pygame.init()
pygame.display.set_caption("SPACE WAR")
display_surface = pygame.display.set_mode((W, H))
while True:
    clock = pygame.time.Clock()
    pygame.time.delay(100)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            done = True
            while done:
                display_surface.fill((0,0,0))
                shoot = pygame.draw.circle(display_surface, YELLOW, (x, y2), 5)
                pygame.display.update()
                y2 -= 5
                print(y2)
                clock.tick(60)
                display_surface.fill((0,0,0))
                if y2 == 0:
                    y2 = 650
                    done = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 10 if x > 20 else 0
    if keys[pygame.K_RIGHT] :
        x += 10 if x < W - 20 else 0
    display_surface.fill((0,0,0))
    space = pygame.image.load('spaceship.jpg')
    display_surface.blit(space, (x, y))
    pygame.display.update() 
    


