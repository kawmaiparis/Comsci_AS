import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
window = pygame.display.set_mode((500, 500))
x, y, move_x, move_y = 0, 0, 0, 0
width, height = 40,40

while True:
    window.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit();sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:move_x += 1
            if event.key == pygame.K_LEFT:move_x -= 1
            if event.key == pygame.K_UP:move_y -= 1
            if event.key == pygame.K_DOWN:move_y += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:move_x = 0
            if event.key == pygame.K_LEFT:move_x = 0
            if event.key == pygame.K_UP:move_y = 0
            if event.key == pygame.K_DOWN:move_y = 0

    x += move_x
    y += move_y
    pygame.draw.rect(window,(100,0,100),(x+300,y+150,width,height))

    pygame.display.update()
