### SRC - Your file didn't have a "py" extension so I have added that.
### This is a good effort, but he parabola looks a bit shallow. Can you get it
### to curve more? It would be good to add some more detail like a blue sky, roof etc.

import pygame
# -- Global Constants   
 
# -- Colours   
BLACK = (0, 0, 0)   
WHITE = (255, 255, 255)   
BLUE = (50, 50, 255)   
YELLOW = (255, 255, 0)   
 
# -- Initialise PyGame 
pygame.init()   
 
# -- Blank Screen   
size = (640, 480)   

 
screen = pygame.display.set_mode(size)   
# -- Title of new window/screen   
pygame.display.set_caption("My Window")   
# -- Exit game flag set to false   
done = False
# -- Declare sun start point
sun_x = 0
sun_y = 100
# -- Manages how fast screen refreshes   
clock = pygame.time.Clock() 

### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # End If
    # Next event
    if sun_x == 640:
        sun_x = 0
    #End If
    # Next Event
    # -- Game logic goes after this comment
    sun_x = sun_x + 1
    sun_y = int(0.0001953125 * sun_x**2 - 0.125 * sun_x + 100)
    # -- Screen background is BLACK
    screen.fill(BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220, 165, 200, 150))
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y), 40, 0)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
### End While - End of game loop
pygame.quit()
