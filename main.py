import pygame
import sys
from src.hero.hero import Hero
from src.card.card import Card
import os

#Inicializa pygame
pygame.init()
#Crea la ventana
screen = pygame.display.set_mode((800, 600))

#Crea el titulo de la ventana
pygame.display.set_caption("Last Dream")

current_dir = os.path.dirname(os.path.abspath(__file__))

# Crea un reloj para controlar el tiempo
clock = pygame.time.Clock()

#Crea el heroe
hero = Hero(screen,current_dir)

card = Card()

#Crea un loop para pygame
while True:
    #Obtiene los eventos de pygame
    for event in pygame.event.get():
        #Si se presiona el boton de cerrar la ventana, se cierra el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    hero.move()

    screen.fill((0, 0, 0))
    hero.animate()
    # Actualiza la pantalla
    pygame.display.flip()

    # 60 fotogramas por segundo
    clock.tick(60)
