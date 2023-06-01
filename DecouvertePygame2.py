## https://openclassrooms.com/forum/sujet/pygame-deux-evenements-a-la-fois-97736
## https://www.pygame.org/docs/

# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init() ## NE PAS OUBLIEZ

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1024, 768))

## Chargement du SysFont
font = pygame.font.SysFont('helvetic', 70)

#Nommer la fenetre
pygame.display.set_caption("Essai")



#Chargement du personnage
personnage = pygame.image.load("Img/left_1.png").convert_alpha()
personnage_rect = personnage.get_rect() ## connaitre le rectangle du personnage

# variable initialisation
continuer = True
TEXT = 'Rien..'
xp=500
yp=500

def gerer_event(x1,y1,tab):
    cont=True



    for event in pygame.event.get():
        if event.type == QUIT:
             cont = False
        #if (event.type == KEYDOWN):
        k = pygame.key.get_pressed()
        if k[K_RIGHT]:
            x1=x1+10
        if k[K_DOWN]:
            y1=y1+10
        if k[K_LEFT]:
            x1=x1-10
            tab[0]=tab[0]+1
            if tab[0]>2 :
                tab[0]=0
        if k[K_UP] :
            y1=y1-10

    ## Si le focus est sur la fenêtre.
    if pygame.mouse.get_focused():
        ## Trouve position de la souris
        x, y = pygame.mouse.get_pos()

        ## S'il y a collision:
        collide = personnage_rect.collidepoint(x-50, y-50)

        if collide:
            texte = 'JE SUIS DESSUS'
        else:
            texte= 'Rien..'

        ## Détecte les clics de souris.
        pressed = pygame.mouse.get_pressed()
        if pressed[0]: # 0=gauche, 1=milieu, 2=droite
            cont = False
    return cont, x1,y1

tab=[0,0]
position_gauche=["left_1.png","left_2.png","left_3.png"]
while continuer:
    fenetre.fill( (120,255,255) )
    personnage = pygame.image.load("Img/"+position_gauche[tab[0]]).convert_alpha()
    fenetre.blit(personnage, (xp, yp))


    text = font.render(TEXT, 1, (120,140,255))
    fenetre.blit(text, (50, 500))

    ## Gérer les événements.
    continuer, xp, yp = gerer_event(xp,yp,tab)

    #Rafraichissement
    pygame.display.flip()

pygame.quit()