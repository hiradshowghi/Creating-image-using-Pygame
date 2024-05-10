#Hirad Showghi Sarkhosh 
#101272774

#Making the background

import pygame

pygame.init()

screen=pygame.display.set_mode((480,640))

white=(255,255,255)

display=pygame.color.Color(white)

screen.fill(display)

#Making first shape

pygame.draw.polygon(screen,(96,102,92),[(0,0),(160,0),(240,106),(0,106)])

#Making second shape

pygame.draw.polygon(screen,(45,52,66),[(0,320),(0,428),(80,534),(160,534)])

pygame.display.update()

pygame.image.save(screen,"assigned_image_for_101272774.png")



