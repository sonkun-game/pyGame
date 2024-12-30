import pygame

class enemy:
    
    # Vị trí đứng của nhân vật
    position_x = 0
    position_y = 0
    
    # Tốc độ di chuyển lên và xuống của nhân vật
    speedX = 0
    speedY = 0
    negative_speedX = 0
    negative_speedY = 0
    
    # link ảnh nhân vật
    image = ''
    is_alive = True
    
    def __init__(self, position_x, position_y, speedX, speedY, image):
        self.position_x = position_x 
        self.position_y = position_y
        self.speedX = speedX
        self.negative_speedX = speedX * -1
        self.speedY = speedY
        self.negative_speedY = speedY * -1
        self.image = image
        
    # Load nhân vật vào pygame
    def enemyImage(self) :
        return pygame.image.load(self.image)
        