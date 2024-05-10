import pygame
import math
import sys

pygame.init()
width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Heptagon")

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 255, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


radius = 150
center= (width // 2, height // 2)

def draw_object(surface):
    points = []
    n = 7
    for i in range(n):
        angle = math.radians(i * 360 / n)
        x = center[0] + int(radius * math.cos(angle))
        y = center[1] + int(radius * math.sin(angle))
        points.append((x, y))
    
    pygame.draw.polygon(surface, BLUE, points, 0)

heptagon = pygame.Surface((width, height))
draw_object(heptagon)
win.blit(heptagon, (0, 0))
pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    scaled = pygame.transform.scale(heptagon, (width * 0.35, height * 0.35))
                    win.fill(BLACK)
                    win.blit(scaled, ((width - scaled.get_width()) // 2, (height - scaled.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_2:
                    rotated = pygame.transform.rotate(heptagon, 45)
                    win.fill(BLACK)
                    win.blit(rotated, ((width - rotated.get_width()) // 2, (height - rotated.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_3:
                    flipped = pygame.transform.flip(heptagon,0,1)
                    win.fill(BLACK)
                    win.blit(flipped,((width - flipped.get_width()) // 2, (height - flipped.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_4:
                    scale = pygame.transform.scale_by(heptagon,(0.35, 1))
                    rotozoom = pygame.transform.rotozoom(scale, 45, 1)
                    win.fill(BLACK)
                    win.blit(rotozoom,((width - rotozoom.get_width()) // 2, (height - rotozoom.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_5:
                    top_scaled = pygame.transform.scale(heptagon, (width, height * 0.35))
                    win.fill(BLACK)
                    win.blit(top_scaled,((width - top_scaled.get_width()) // 2, 1))
                    pygame.display.flip()
                elif event.key == pygame.K_6:
                    scaled_2 = pygame.transform.scale_by(heptagon,(0.35, 1))
                    rotozoom = pygame.transform.rotozoom(scaled_2, 180, 1)
                    win.fill(BLACK)
                    win.blit(rotozoom,((width - rotozoom.get_width()) // 2, (height - rotozoom.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_7:
                    scaled_3 = pygame.transform.scale_by(heptagon, (0.5,1))
                    flip = pygame.transform.flip(scaled_3, 1,0)
                    win.fill(BLACK)
                    win.blit(flip, ((width - flip.get_width()) // 2, (height - flip.get_height()) // 2))
                    pygame.display.flip()
                elif event.key == pygame.K_8:
                    scaled_4 = pygame.transform.scale_by(heptagon, (1,0.4))
                    rotated_2 = pygame.transform.rotate(scaled_4, -20)
                    win.fill(BLACK)
                    win.blit(rotated_2, ((width - rotated_2.get_width()) * 1.2, (height - rotated_2.get_height()) * 1.5))
                    pygame.display.flip()
                elif event.key == pygame.K_9:
                    scaled_5 = pygame.transform.scale_by(heptagon,(0.35, 1))
                    rotozoom = pygame.transform.rotozoom(scaled_5, 90, 1)
                    win.fill(BLACK)
                    win.blit(rotozoom,((width - rotozoom.get_width() +250) // 2, (height - rotozoom.get_height()) //2))
                    pygame.display.flip()
                else:
                    win.fill(BLACK)
                    draw_object(win)
                    win.blit(win, (0,0))
                    pygame.display.flip()
                    

    pygame.display.update()