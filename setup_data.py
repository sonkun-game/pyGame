import pygame

class setup_data: 
    # screen config
    screen_width = 1280
    screen_height = 720

    FPS = 60

    title = "Hoang Son game"
    icon = 'viking-head.png'
    background = './img/ground.jpg'
    
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    enemy_is_running = True