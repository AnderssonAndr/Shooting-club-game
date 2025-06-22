import pygame
import random
#random.init
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = (pygame.display.set_mode
         ((SCREEN_WIDTH, SCREEN_HEIGHT)))
# наружные скобки нужны для переноса строки
color = ((random.randint(0,255), 
      random.randint(0,255), random.randint(0,255)))
# color is a tuple of Red, Green and Blue
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Дартс.png") 
pygame.display.set_icon(icon) # устанавливает загруженное 
# изображение, как иконку для игры.
target_image = pygame.image.load("img/Apple_target.png")
target_width = 96 # is a real size of downloaded and
target_height = 96 # saved png-image!!! 
target_x =(random.randint(0, 
          SCREEN_WIDTH - target_width))
target_y = (random.randint(0, 
          SCREEN_HEIGHT - target_height))
# обе координаты мишени (они стартовые!) необходимо 
# задать до их использования в цикле (см ниже)
running = True 
while running:
    screen.fill(color)
    for event in pygame.event.get():# цикл перебирает 
    #все происходящие события 
        if event.type == pygame.QUIT:# это нажатие
            # на крестик
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:  
            mouse_x, mouse_y = pygame.mouse.get_pos()
# определяет координаты клика мышки (кортеж get_pos()...)
            if (target_x < mouse_x < target_x + 
                target_width 
            and target_y < mouse_y < target_y + 
                target_height):
            # крайние скобки для переноса        
                #pass # добавить очко
                # добавить ещё 2 объекта разной стоимости
                # добавить время игры        
                target_x = (random.randint
                (0, SCREEN_WIDTH - target_width))
                target_y = (random.randint
                (0, SCREEN_HEIGHT - target_height))
    # это следующие случайные координаты
    screen.blit(target_image, (target_x, target_y))
    # поместили мишень на экран
    pygame.display.update()
    # обновление экрана
#pygame.quit()    
