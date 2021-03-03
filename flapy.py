import pygame, random,time

pygame.font.init()
pygame.init() # Inicializamos pygame
size = 1920,1080  # Muestro una ventana de 800x600
screen = pygame.display.set_mode(size)
pos_x=100
pos_y=300
background=pygame.image.load("wall.png")
run=True  # Comenzamos el bucle del juego
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
contador=0
flap=pygame.image.load("flap.png").convert()
flap.set_colorkey(black)
flap=pygame.transform.scale(flap,[50,30])
flaprect=flap.get_rect()
fuerza_x=0
fuerza_y=0
#tuberia
tube_width=60
tube_height=random.randint(100,900)
tube_height2=random.randint(100,900)
tube_color=green
tube_x=1920
tube_x2=2840
score=0
flaprect=flaprect.move(pos_x,pos_y)
fuente=pygame.font.SysFont("Calibri", 34, True, False)
hueco=250
correct=False
def tube():
    pygame.draw.rect(screen,(green),(tube_x,0,tube_width,tube_height))
    pygame.draw.rect(screen,(green),(tube_x,tube_height+hueco, tube_width,1080))
    pygame.draw.rect(screen,(green),(tube_x2,0,tube_width,tube_height2))
    pygame.draw.rect(screen,(green),(tube_x2,tube_height2+hueco, tube_width,1080))
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Salgo de pygame
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                fuerza_y=-4
    fuerza_y+=0.05
    tube_x+=-2
    tube_x2+=-2
    if tube_x<=-10:
        tube_x=1920
        tube_height=random.randint(100,900)
        score+=1
    if tube_x2<=-10:
        tube_x2=1920
        tube_height2=random.randint(100,900)
        score+=1
        print(score)
    #ZONA DIBUJO
    flaprect=flaprect.move(fuerza_x,fuerza_y)
    screen.blit(background, (0,0))
    screen.blit(flap, flaprect)
    tube()
    text=fuente.render(str(score),True,white)
    screen.blit(text,[10,10])
    pygame.display.flip()
    if tube_x<100:
        if pos_y<tube_height:
            pygame.quit()
        if pos_y>tube_height+hueco:
            pygame.quit()
    if tube_x2<100:
        if pos_y<tube_height2:
            pygame.quit()
        if pos_y>tube_height2+hueco:
            pygame.quit()
    pos_y += fuerza_y
    if pos_y>1100 or pos_y<-80:
        pygame.quit()