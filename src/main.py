import pygame
import sys

#Inicializa pygame
pygame.init()
#Crea la ventana
screen = pygame.display.set_mode((800, 600))

#Crea un loop para pygame
while True:
    #Obtiene los eventos de pygame
    for event in pygame.event.get():
        #Si se presiona el boton de cerrar la ventana, se cierra el programa
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Actualiza la pantalla
    pygame.display.update()