import pygame
import sys
from hero.hero import Hero
from card.card import Card
import os
from hand.hand import Hand

#Inicializa pygame
pygame.init()
#Crea la ventana
screen = pygame.display.set_mode((800, 600))

#Crea el titulo de la ventana
pygame.display.set_caption("Last Dream")

current_dir = os.path.dirname(os.path.abspath(__file__))

# Crea un reloj para controlar el tiempo
clock = pygame.time.Clock()

card = Card("assets/card/assets_cards.png", 5, None)

hand = Hand(screen)
hand.add_card(card)

#Crea un loop para pygame
while True:
    #Obtiene los eventos de pygame
    for event in pygame.event.get():
        #Si se presiona el boton de cerrar la ventana, se cierra el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    hand.draw()

    # Actualiza la pantalla
    pygame.display.flip()

    # 60 fotogramas por segundo
    clock.tick(60)
