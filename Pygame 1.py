import pygame 
pygame.init() 
window = pygame.display.set_mode((500,400)) 
while True: 
    pygame.draw.rect(window, (255,0,0),(0,0,80,80)) 
    pygame.draw.rect(window, (0,255,0),(30,30,80,80)) 
    pygame.draw.rect(window, (0,0,255),(60,60,100,100)) 
    pygame.draw.circle(window, (255,255,0), (250,200), 20, 0) 
    pygame.draw.ellipse(window, (255,0,255), (100,100,100,50)) 
    pygame.draw.line(window, (255,255,255), (0,0), (500,400), 1) 
    pygame.display.update() 
