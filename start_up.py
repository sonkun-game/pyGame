import pygame
import random
import math
from setup_data import setup_data as st
from player import player
from enemy import enemy
from bullet import bullet

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((st.screen_width, st.screen_height))
clock = pygame.time.Clock()
running = True

# Title and Icon
pygame.display.set_caption(st.title)
icon = pygame.image.load(st.icon)
pygame.display.set_icon(icon)

# Score 
textX = 10
textY = 10
font = pygame.font.Font('freesansbold.ttf', 32)

# background
background = pygame.image.load(st.background)

# Warrior
warrior = player(580, 400, 5, 5, './img/knight.png')
changeX = 0
changeY = 0

# Bullet
fireball = bullet(0, 480, 5, 5, './img/fire.png')
bulletX = 0
bulletY = 10

# Enemy
cthulhu = enemy(random.randint(0, st.screen_width), random.randint(50, 150), 5, 5, './img/cthulhu.png')
enemyX = 5
enemyY = 5
enemy_is_running = st.enemy_is_running

listEnemyLabel = ['./img/cthulhu.png', './img/werewolf.png', './img/monster.png']
listEnemy = []
listEnemyX = []
listEnemyY = []
number_of_enemy = 3

for i in range(number_of_enemy) :
    if i <= len(listEnemyLabel) :
        listEnemy.append(enemy(random.randint(0, st.screen_width), random.randint(50, 150), 5, 5, listEnemyLabel[i]))
    else :
        listEnemy.append(enemy(random.randint(0, st.screen_width), random.randint(50, 150), 5, 5, './img/cthulhu.png'))
    listEnemyX.append(5)
    listEnemyY.append(5)

def showScore(x, y) :
    score = font.render("Score : " + str(st.score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def playerRunning(x, y) :
    image = warrior.playerImage()
    screen.blit(image, (x, y))

def enemyRunning(x, y, i) :
    if listEnemy[i].is_alive :
        image = listEnemy[i].enemyImage()
        screen.blit(image, (x, y))

def fireBullet(x, y):
    fireball.bullet_state = 'fire'
    fireball.position_x = x
    image= fireball.bulletImage()
    screen.blit(image, (x + 16, y + 10))
    
def isGotHit(monster: enemy, fireball: bullet):
    distance = math.sqrt(math.pow(monster.position_x - fireball.position_x , 2) + math.pow(monster.position_y - fireball.position_y, 2))
    if distance <= 60 :
        return True
    else :
        return False
        
    
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
                    bulletX = warrior.position_x
                    fireBullet(bulletX, fireball.position_y)
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
    
    if warrior.position_x <= 0:
        warrior.position_x = 0
    elif warrior.position_x > (st.screen_width - 100) :
        warrior.position_x = (st.screen_width - 100)
    

    # Enemy running
    if enemy_is_running :

        for i in range(number_of_enemy):
            listEnemy[i].position_x += listEnemyX[i]
            listEnemy[i].position_y += listEnemyY[i]

            if listEnemy[i].position_x <= 0 :
                listEnemyX[i] = listEnemy[i].speedX
            elif listEnemy[i].position_x >= st.screen_width :
                listEnemyX[i] = listEnemy[i].negative_speedX

            if listEnemy[i].position_y <= 0 :
                listEnemyY[i] = listEnemy[i].speedY
            elif listEnemy[i].position_y >= st.screen_height :
                listEnemyY[i] = listEnemy[i].negative_speedY

            # enemy got hit by fireball
            is_got_hit = isGotHit(listEnemy[i], fireball)
    
            if is_got_hit and fireball.bullet_state is 'fire' :
                fireball.position_y = 480
                fireball.bullet_state = 'ready'
                st.score_value += 1
                listEnemy[i].is_alive = False

            enemyRunning(listEnemy[i].position_x, listEnemy[i].position_y, i)

    # Fireball shooting
    if fireball.position_y <= 0:
        fireball.position_y = 480
        fireball.bullet_state = "ready"

    if fireball.bullet_state is 'fire' :
        fireBullet(bulletX, fireball.position_y)
        fireball.position_y -= bulletY
        
    # render
    playerRunning(warrior.position_x, warrior.position_y)
    showScore(textX, textY)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(st.FPS)  # limits FPS to 60

pygame.quit()
