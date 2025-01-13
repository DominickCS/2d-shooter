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
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


time = 0

laser_list = pygame.sprite.Group()
player = pygame.sprite.Group()
turretOne = Turret("White", 20, 20, 0, x=450, y=300)
# turretOne.rect.x = 450
# turretOne.rect.y = 300
player.add(turretOne)
while True:
    time
    B = pygame.mouse.get_pos()
    # Statement below is angle debug 
    screen.fill("BLACK")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements, and update game aspects
    player.draw(screen)
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Clock Debugging
        # print(pygame.time.get_ticks())
        # print(time)
        if pygame.time.get_ticks() > time:
            if len(laser_list) <=1:
                print(calculate_angle(A,B))
                project_angle = ((calculate_angle(A,B)))
                print("shooting")
                laser = Turret("White", 5, 5, project_angle , 450, 300)
                laser_list.add(laser)

                time = pygame.time.get_ticks() + 500
                # print(len(laser_list))
                # laser.rect.y = random.randint(0, 600)
                #pygame.time.delay(100)
    for laser in laser_list:
            laser_list.draw(screen)
            pygame.display.update()
            laser.rect.x += 5 * math.cos(laser.angle)
            laser.rect.y += 5 * math.sin(laser.angle)
            # print(laser.rect.x)
            # print(laser.rect.y)
            if laser.rect.x >= 900:
                laser.kill()
                print(len(laser_list))
    pygame.display.update()
    clock.tick(60)