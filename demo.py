# Example file showing a basic pygame "game loop"
import pygame
from player import player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Title and Icon
pygame.display.set_caption("Hoang Son game")
icon = pygame.image.load('viking-head.png')
pygame.display.set_icon(icon)

# Movement
player_speed = 20
changeX = 0
changeY = 0

# Warrior
warrior = player(580, 400, 5, 5, 'knight.png')

def player(x, y) :
    image = warrior.playerImage()
    screen.blit(image, (x, y))
    
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeY = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((125, 186, 102))

    # RENDER YOUR GAME HERE
    warrior.position_x += changeX
    warrior.position_y += changeY
    player( warrior.position_x, warrior.position_y)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
