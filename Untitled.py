 #! /usr/bin/env python
 2 
 3 # Move a single pixel around the screen without crashing against the borders.
 4 
 5 import pygame
 6 
 7 # Window dimensions.
 8 width = 640
 9 height = 400
10 
11 # Position of the pixel.
12 x = width / 2
13 y = height / 2
14 
15 # Direction of the pixel.
16 dir_x = 0
17 dir_y = -1
18 
19 screen = pygame.display.set_mode((width, height))
20 clock = pygame.time.Clock()
21 running = True
22 
23 while running:
24     x += dir_x
25     y += dir_y
26 
27     if x <= 0 or x >= width or y <= 0 or y >= height:
28         print "Crash!"
29         running = False
30 
31     screen.fill((0, 0, 0))
32     screen.set_at((x, y), (255, 255, 255))
33     
34     for event in pygame.event.get():
35         if event.type == pygame.QUIT:
36             running = False
37         elif event.type == pygame.KEYDOWN:
38             if event.key == pygame.K_UP:
39                 dir_x = 0
40                 dir_y = -1
41             elif event.key == pygame.K_DOWN:
42                 dir_x = 0
43                 dir_y = 1
44             elif event.key == pygame.K_LEFT:
45                 dir_x = -1
46                 dir_y = 0
47             elif event.key == pygame.K_RIGHT:
48                 dir_x = 1
49                 dir_y = 0
50 
51     pygame.display.flip()
52     clock.tick(120)
