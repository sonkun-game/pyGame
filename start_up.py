import pygame
import random
from setup_data import setup_data as st
from player import player
from enemy import enemy
from bullet import bullet

# pygame setup
pygame.init()
screen = pygame.display.set_mode((st.screen_width, st.screen_height))
clock = pygame.time.Clock()
running = True

# Title and Icon
pygame.display.set_caption(st.title)
icon = pygame.image.load(st.icon)
pygame.display.set_icon(icon)

# background
background = pygame.image.load(st.background)

# Warrior
warrior = player(580, 400, 5, 5, './img/knight.png')
changeX = 0
changeY = 0

# Bullet
fireball = bullet(0, 400, 40, 40, './img/fire.png')
bulletY = 10

# Enemy
cthulhu = enemy(random.randint(0, st.screen_width), random.randint(50, 150), 5, 5, './img/cthulhu.png')
enemyX = 5
enemyY = 5

def playerRunning(x, y) :
    image = warrior.playerImage()
    screen.blit(image, (x, y))

def enemyRunning(x, y) :
    image = cthulhu.enemyImage()
    screen.blit(image, (x, y))

def fireBullet(x, y):
    fireball.bullet_state = 'fire'
    image= fireball.bulletImage()
    screen.blit(image, (x + 16, y + 10))
    
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = warrior.negative_speedX
            if event.key == pygame.K_RIGHT:
                changeX = warrior.speedX 
            if event.key == pygame.K_UP:
                changeY = warrior.negative_speedY
            if event.key == pygame.K_DOWN:
                changeY = warrior.speedY
            if event.key == pygame.K_SPACE:
                if fireball.bullet_state is "ready":
                    fireBullet(warrior.position_x, fireball.position_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeY = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((73, 130, 196))

    # background
    # screen.blit(background, (0,0))

    # RENDER YOUR GAME HERE

    # Warrior running
    warrior.position_x += changeX
    warrior.position_y += changeY
    

    # Enemy running
    cthulhu.position_x += enemyX
    cthulhu.position_y += enemyY

    if cthulhu.position_x <= 0 :
        enemyX = cthulhu.speedX
    elif cthulhu.position_x >= st.screen_width :
        enemyX = cthulhu.negative_speedX

    if cthulhu.position_y <= 0 :
        enemyY = cthulhu.speedY
    elif cthulhu.position_y >= st.screen_height :
        enemyY = cthulhu.negative_speedY

    if fireball.position_y <= -10:
        fireball.position_y = 400
        fireball.bullet_state = "ready"

    if fireball.bullet_state is 'fire' :
        fireBullet(warrior.position_x, fireball.position_y)
        fireball.position_y -= bulletY

    # render
    playerRunning(warrior.position_x, warrior.position_y)
    enemyRunning(cthulhu.position_x, cthulhu.position_y)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(st.FPS)  # limits FPS to 60

pygame.quit()
