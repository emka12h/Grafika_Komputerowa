import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
NIEBIESKI = (0, 0, 255)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # rysowanie kwadratów
    pygame.draw.rect(win, NIEBIESKI , (200, 200, 200, 100))

    #rysowanie trójkąta (dolnego)
    pygame.draw.polygon(win, NIEBIESKI, [(300, 300), (250, 400), (350, 400)])

    #rysowanie trójkąta (górny)
    traingle2=pygame.draw.polygon(win,NIEBIESKI, [(300,200), (250,100),(350,100)])
   
    
    pygame.display.update()