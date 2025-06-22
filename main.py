import pygame
import random
random.init
pygame.init
running = True
while running:
    pass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = (pygame.display.set_mode
         ((SCREEN_WIDTH, SCREEN_HEIGHT))) 
#наружные скобки
#нужны для переноса строки
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Дартс.png") 
pygame.display.set_icon(icon) #устанавливает загруженное 
# изображение, как иконку для игры.
target_image = pygame.image.load("img/Apple_target.png")
target_width = 50
target_height = 50
target_x =(random.randint(0, 
          SCREEN_WIDTH - target_width))
target_y = (random.randint(0, 
           SCREEN_HEIGHT - target_height))
color = ((random.randint(0,255), 
      random.randint(0,255), random.randint(0,255)))
#color is a tuple of Red, Green and Blue
