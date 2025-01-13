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
    angle = math.degrees(angle)  # convert to degrees
    return angle + 360 if angle < 0 else angle

A = (450, 300)

class Turret(pygame.sprite.Sprite):
    def __init__(self, color, height, width, x=0, y=0):
        super().__init__()

        #pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #self.image.set_colorkey("White")

        pygame.draw.rect(self.image, color, pygame.Rect(x,y, width, height))
        self.rect = self.image.get_rect()

laser_list = pygame.sprite.Group()
player = pygame.sprite.Group()
turretOne = Turret("White", 20, 20)
laser = Turret("White", 10, 1)
turretOne.rect.x = 450
turretOne.rect.y = 300
player.add(turretOne)
while True:
    B = pygame.mouse.get_pos()
    # Statement below is angle debug 
    # project_angle = print(round((calculate_angle(A,B))))
    screen.fill("BLACK")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements, and update game aspects
    player.draw(screen)
    if event.type == pygame.MOUSEBUTTONDOWN:
        #print("shooting")
        #player_sprite_list.add(laser)
        if len(laser_list) <= 2:
            laser_list.add(laser)
            print("shooting")
            # laser.rect.y = random.randint(0, 600)
            laser_list.draw(screen)
            pygame.display.update()
            #pygame.time.delay(100)
    for laser in laser_list:
            laser.rect.x = laser.rect.x + 5
            if laser.rect.x >= 900:
                laser.kill()
                print(len(laser_list))
    pygame.display.update()
    clock.tick(60)