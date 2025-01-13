import pygame
import random
import numpy as np
import math
from sys import exit

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("zombies")
clock = pygame.time.Clock()

def calculate_angle(p1, p2) -> float:
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    angle = math.atan2(dy, dx)  # radians
    # angle = math.degrees(angle)  # convert to degrees
    return angle
    # (move above if not working) + 360 if angle < 0 else angle

A = (450, 300)

class Turret(pygame.sprite.Sprite):
    def __init__(self, color, height, width, rad , x, y):
        super().__init__()
        self.angle = rad
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.internal_x = float(x)
        self.internal_y = float(y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        


time = 0
score = 0


laser_list = pygame.sprite.Group()
player = pygame.sprite.Group()

enemies = pygame.sprite.Group()

turretOne = Turret("White", 16, 16, 0, x=450-16/2, y=300-16/2)

player.add(turretOne)
while True:
    # Debug Mouse Position Coords
    # print(pygame.mouse.get_pos())
    time
    B = pygame.mouse.get_pos()
    # Statement below is angle debug 
    screen.fill("BLACK")
    enemies.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements, and update game aspects
    if len(enemies) <= 5:
        print(len(enemies))
        enemies.add(Turret("RED", 16, 16, 0, random.randint(0, 900), random.randint(0,600)))

    pygame.sprite.groupcollide(laser_list, enemies, False,  True)
    player.draw(screen)
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        # Clock Debugging
        # print(pygame.time.get_ticks())
        # print(time)
        if pygame.time.get_ticks() > time:
            # Check laser amount
            # print(len(laser_list))
            if len(laser_list) <=20:
                # Print laser angle
                # print(calculate_angle(A,B))
                project_angle = ((calculate_angle(A,B)))
                laser = Turret("White", 4, 4, project_angle , turretOne.rect.x + 4, turretOne.rect.y + 4)
                laser_list.add(laser)
                time = pygame.time.get_ticks() + 200

    for laser in laser_list:
            laser_list.draw(screen)
            pygame.display.update()
            laser.internal_x += 8 * math.cos(laser.angle)
            laser.internal_y += 8 * math.sin(laser.angle)
            laser.rect.x = laser.internal_x
            laser.rect.y = laser.internal_y
            # print(laser.rect.x)
            # print(laser.rect.y)
            if laser.rect.x >= 900:
                laser.kill()
            if laser.rect.x <= 0:
                laser.kill()
            if laser.rect.y >= 600:
                laser.kill()
            if laser.rect.y <= 0:
                laser.kill()
    pygame.display.update()
    clock.tick(60)