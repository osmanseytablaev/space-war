import pygame
import random
import datetime as dt

pygame.init()
ship_x = 450
ship_y = 650
gun_x = ship_x + 24
gun_y = ship_y
enemy_x = random.randint(1, 500)
enemy_y = 0.99
size = 40
bullets = []
enemies = []
pygame.mixer.music.load('Audio/A4.mp3')
pygame.mixer.music.play()
w = 900
h = 700
pygame.display.set_caption("SPACE WAR")
screen = pygame.display.set_mode((w, h))
time = dt.datetime.now()
time_game = dt.datetime.now()
score_value = 0
YELLOW = 255, 255, 0


while True:
    date_game = dt.datetime.now() - time_game
    if date_game.seconds >= 300:  # 60 * 5 = 300 sec = 5 min game
        print('Game end')
        break
    date = dt.datetime.now() - time
    if date.seconds >= 5:
        enemies.append((random.randint(1, 800), enemy_y))
        time = dt.datetime.now()
    f1 = pygame.font.SysFont('serif', 16)
    text1 = f1.render("Score:" + str(score_value), True,
                      YELLOW)
    screen.blit(text1, (820, 670))
    gun_x = ship_x
    gun_y = ship_y
    ship = pygame.image.load('Images/ship.png')
    screen.blit(ship, (ship_x, ship_y))
    pygame.display.flip()
    screen.fill((0, 0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        ship_x -= 2 if ship_x > 20 else 0
    elif pressed[pygame.K_RIGHT]:
        ship_x += 2 if ship_x < w - 20 else 0
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            bullets.append((gun_x, gun_y))
            pygame.mixer.music.load('Audio/boom.mp3')
            pygame.mixer.music.play()
    for bullet in bullets:
        pygame.draw.rect(screen,
                         (254, 52, 110),
                         pygame.Rect(gun_x, gun_y, 2, 4))
        gun_y -= 5
    for enemy_state in enemies:
        enemy = pygame.image.load('Images/enemy.png')
        screen.blit(enemy, (enemy_x, enemy_y))
        enemy_y += 0.20
        for bullet in bullets:
            if (enemy_x + size > bullet.gun_x > enemy_x - size and
                    enemy_y + size > bullet.gun_y > enemy_y - size):
                bullets.remove(bullet)
                # noinspection PyArgumentList
                enemies.remove()
                pygame.mixer.music.load('Audio/boom2.mp3')
                pygame.mixer.music.play()
                score_value += 1
                screen.blit(text1, (820, 670))