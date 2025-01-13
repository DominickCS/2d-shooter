import pygame
from pygame import mixer
import random
import numpy as np
import math
from sys import exit

pygame.font.init() 
my_font = pygame.font.SysFont('Arial', 30)

# Initialize audio
mixer.init()
shoot = mixer.music.load("shoot.wav", "hit.wav")
mixer.Channel(1).set_volume(.3) 
mixer.Channel(0).set_volume(.3)

# Initialize PyGame
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
        

# Constant Intitialzation
time = 0
score = 0
laser_list = pygame.sprite.Group()
player = pygame.sprite.Group()
enemies = pygame.sprite.Group()
turretOne = Turret("White", 16, 16, 0, x=450-16/2, y=300-16/2)
player.add(turretOne)

while True:
    scoreboard = my_font.render(f"Score: {score}", False, "White")
    # Debug Mouse Position Coords
    # print(pygame.mouse.get_pos())
    time
    B = pygame.mouse.get_pos()
    # Fill background with black bg
    screen.fill("BLACK")
    # Adds scoreboard
    screen.blit(scoreboard, (24, 0))
    # Adds enemies list
    enemies.draw(screen)

    # Checks for quitting via "X" button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Main Game Loop & Logic:

    if len(enemies) <= 5:
        # print(len(enemies))
        enemy_y = random.randint(0,600)
        enemy_x = random.randint(0,900)
        binary = random.randint(0,1)

        if binary == 0:
            if enemy_y <300:
                enemy_y = 0
            else:
                enemy_y = 600 - 16 /2
        else:
            if enemy_x <450:
                enemy_x = 0
            else:
                enemy_x = 900  -16 /2
        # Enemy Pathfinding Logic using angle calc function        
        C = (enemy_x, enemy_y)
        enemy_angle = (calculate_angle(A, C))
        # Enemy Template
        enemies.add(Turret("RED", 16, 16, enemy_angle, enemy_x, enemy_y))
    
    # Laser collision Logic
    if pygame.sprite.groupcollide(laser_list, enemies, True,  True):
         mixer.Channel(1).play(pygame.mixer.Sound("hit.wav"))
         score += 100
         print(score)
    # Player Rendering
    player.draw(screen)
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        # Clock Debugging
        # print(pygame.time.get_ticks())
        # print(time)
        if pygame.time.get_ticks() > time:
            mixer.Channel(0).play(pygame.mixer.Sound("shoot.wav"))
            # Check laser amount
            # print(len(laser_list))
            if len(laser_list) <=20:
                # Print laser angle
                # print(calculate_angle(A,B))
                project_angle = ((calculate_angle(A,B)))
                laser = Turret("White", 4, 4, project_angle , turretOne.rect.x + 4, turretOne.rect.y + 4)
                laser_list.add(laser)
                time = pygame.time.get_ticks() + 200

    # Enemy Movement
    for enemy in enemies:
        enemy_angle = (calculate_angle(A, C))
        enemy.internal_x -= 1.25 * math.cos(enemy.angle)
        enemy.internal_y -= 1.25 * math.sin(enemy.angle)
        enemy.rect.x = enemy.internal_x
        enemy.rect.y = enemy.internal_y
        if enemy.rect.x >= 900:
                enemy.kill()
        if enemy.rect.x <= 0:
                enemy.kill()
        if enemy.rect.y >= 600:
                enemy.kill()
        if enemy.rect.y <= 0:
                enemy.kill()
    # Laser Movement
    for laser in laser_list:
            laser_list.draw(screen)
            pygame.display.update()
            laser.internal_x += 16 * math.cos(laser.angle)
            laser.internal_y += 16 * math.sin(laser.angle)
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
       
       # Enemy to player collision logic
    if pygame.sprite.groupcollide(player, enemies, True,  True):
         print(f"The zombies have gotten to you...\nYour Final score was {score}.")
         pygame.quit()
         exit()
    pygame.display.update()
    clock.tick(60)

    #Test